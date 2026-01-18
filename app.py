from fastapi import FastAPI, HTTPException, Header
from typing import List
from pydantic import BaseModel

app = FastAPI()

# stockage en mémoire
patients = []

API_KEY = "secret123"

class Patient(BaseModel):
    name: str

@app.post("/patients")
def add_patient(patient: Patient, api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    patient = {"id": len(patients)+1, "name": patient.name}
    patients.append(patient)
    return patient

@app.get("/patients", response_model=List[dict])
def list_patients():
    return patients
