from sqlalchemy import Column, String, create_engine,Integer,Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Patients(Base):
    __tablename__ = 'patients'
    __tableargs__ = {
        'comment': 'Table with information about patients'
    }

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

    def __repr__(self):
        return f'{self.ID} {self.Status} {self.Age}'

engine = create_engine("postgresql://postgres:mynewpassword@localhost:5432/db_cirrocis")

Base.metadata.create_all(engine)
