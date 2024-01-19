from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    ID = Column(Integer, primary_key=True, index=True)
    N_Days = Column(Integer)
    Status = Column(String)
    Drug = Column(String)
    Age = Column(Integer)
    Sex = Column(String)
    Ascites = Column(String)
    Hepatomegaly = Column(String)
    Spiders = Column(String)
    Edema = Column(String)
    Bilirubin = Column(Float)
    Cholesterol = Column(Float)
    Albumin = Column(Float)
    Copper = Column(Float)
    Alk_Phos = Column(Float)
    SGOT = Column(Float)
    Tryglicerides = Column(Float)
    Platelets = Column(Float)
    Prothrombin = Column(Float)
    Stage = Column(Float)

    treatments = relationship("Treatment", back_populates="patient")

class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.ID'))
    drug = Column(String)
    duration_days = Column(Integer)
    outcome = Column(String)

    patient = relationship("Patient", back_populates="treatments")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'postgresql://username:password@localhost:5432/your_database' with your actual PostgreSQL connection details.

engine = create_engine("postgresql://postgres:mynewpassword@localhost:5432/cirrossis")

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Optionally, you can also create a Session class for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
