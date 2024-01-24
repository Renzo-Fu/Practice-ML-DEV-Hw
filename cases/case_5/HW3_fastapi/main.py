from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from passlib.context import CryptContext
from jose import jwt
from typing import Optional
import pickle
import uvicorn

# --- Database Setup and Models ---
DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    balance = Column(Float, default=0)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# --- User Authentication ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- FastAPI App ---
app = FastAPI()

# ... Your existing code for PredictionInput and model loading ...

# --- User Management Endpoints ---
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# Definición de la función get_db
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for UserCreate
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Create tables in the database
Base.metadata.create_all(bind=engine)


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    fake_hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Define the data model for the prediction input
class PredictionInput(BaseModel):
    N_Days: int
    Age: int
    Bilirubin: float
    Cholesterol: float
    Albumin: float

# Initialize FastAPI app
    
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the machine learning model from the provided .pkl file
with open("cirrhosis_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a POST endpoint for prediction
@app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        # Prepare the feature vector for prediction
        features = [[
            input_data.N_Days,
            input_data.Age,
            input_data.Bilirubin,
            input_data.Cholesterol,
            input_data.Albumin
        ]]
        
        # Perform the prediction
        prediction = model.predict(features)
        
        # Return the prediction result
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test_predict/")
async def test_predict():
    # Dummy data for testing
    test_input = PredictionInput(
        N_Days=100,
        Age=50,
        Bilirubin=1.2,
        Cholesterol=200,
        Albumin=3.5
    )
    return await predict(test_input)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
