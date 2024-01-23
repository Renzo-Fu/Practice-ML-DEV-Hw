from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import pickle
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


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
