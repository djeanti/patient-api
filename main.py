from enum import IntEnum 
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()

class TransplantRecipientBase(BaseModel):
    health_card_number: Optional[str]	= Field(None, min_length=1, max_length=512, description='NAS of patient')
    health_card_issuing_authority: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    last_name: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    first_name: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')
    recipient_id: str	= Field(..., min_length=1, max_length=512, description='See attribute name')		
    recipient_id_issuing_organization: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	
    date_of_birth: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	
    province_of_residence: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    postal_code: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    country_of_residence: str	= Field(..., min_length=1, max_length=512, description='See attribute name')		
    referral_date: str	= Field(..., min_length=1, max_length=512, description='See attribute name')		
    transplant_center: str	= Field(..., min_length=1, max_length=512, description='See attribute name')		
    requested_organs: str	= Field(..., min_length=1, max_length=512, description='See attribute name')			
    pre_discussion_living_donor: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    sex_at_birth: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	
    gender_identity: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    racial_group: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    indigenous_identity: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    blood_type: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    highest_education_level: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    referral_decision: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	
    referral_decision_date: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	
    date_of_death: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    demographics_effective_date: str	= Field(..., min_length=1, max_length=512, description='See attribute name')	

class TransplantRecipientCreate(TransplantRecipientBase):
    pass

class TransplantRecipient(TransplantRecipientBase):
    patient_id: int = Field(..., description='Unique identifier of the patient') 

class TransplantRecipientUpdate(BaseModel):
    health_card_number: Optional[str]	= Field(None, min_length=1, max_length=512, description='NAS of patient')
    health_card_issuing_authority: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    last_name: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    first_name: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')
    recipient_id: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    recipient_id_issuing_organization: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    date_of_birth: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    province_of_residence: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    postal_code: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    country_of_residence: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    referral_date: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    transplant_center: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')		
    requested_organs: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')			
    pre_discussion_living_donor: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    sex_at_birth: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    gender_identity: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    racial_group: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    indigenous_identity: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    blood_type: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    highest_education_level: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    referral_decision: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    referral_decision_date: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    date_of_death: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	
    demographics_effective_date: Optional[str]	= Field(None, min_length=1, max_length=512, description='See attribute name')	

from test_data import all_patients 

@api.get('/patients/{patient_id}', response_model=TransplantRecipient) # equivalent to URL: localhost:9999/todos/2
def get_patient_fromid(patient_id: int):
    for patient in all_patients:
        if patient.patient_id == patient_id:
            return patient
    raise HTTPException(404, detail='Patient not found')

# URL: localhost:9999/todos?first_n=3 -> query parameter is used
@api.get('/patients', response_model=List[TransplantRecipient])
def get_patients(first_n: int = None): # Get me the first N patients
    if first_n:
        return all_patients[:first_n]
    else:
        return all_patients

@api.post('/patients', response_model=TransplantRecipient)
def create_patient(patient: TransplantRecipientCreate):
    new_patient_id = len(all_patients)+1
    new_patient = TransplantRecipient(
        patient_id=new_patient_id,
        health_card_number=patient.health_card_number,
        health_card_issuing_authority=patient.health_card_issuing_authority,
        last_name=patient.last_name,
        first_name=patient.first_name,
        recipient_id=patient.recipient_id,
        recipient_id_issuing_organization=patient.recipient_id_issuing_organization,
        date_of_birth=patient.date_of_birth,
        province_of_residence=patient.province_of_residence,
        postal_code=patient.postal_code,
        country_of_residence=patient.country_of_residence,
        referral_date=patient.referral_date,
        transplant_center=patient.transplant_center,
        requested_organs=patient.requested_organs,
        pre_discussion_living_donor=patient.pre_discussion_living_donor,
        sex_at_birth=patient.sex_at_birth,
        gender_identity=patient.gender_identity,
        racial_group=patient.racial_group,
        indigenous_identity=patient.indigenous_identity,
        blood_type=patient.blood_type,
        highest_education_level=patient.highest_education_level,
        referral_decision=patient.referral_decision,
        referral_decision_date=patient.referral_decision_date,
        date_of_death=patient.date_of_death,
        demographics_effective_date=patient.demographics_effective_date
    )

    all_patients.append(new_patient)   
    return new_patient

#PATCH vs PUT: PUT = remplacmeent complet selon norme HTTP mais PATCH = remplacement partiel( que avec les champs fourni)
@api.patch('/patients/{patient_id}', response_model=TransplantRecipient)
def update_patient(patient_id: int, updated_patient: TransplantRecipientUpdate):
    for patient in all_patients:
        if patient.patient_id == patient_id:
            allowed_fields = updated_patient.dict(exclude_unset=True)
            for field, value in allowed_fields.items():
                if field != "patient_id":
                    setattr(patient, field, value)
            return patient
    raise HTTPException(404, detail='Patient not found')

@api.put('/patients/{patient_id}', response_model=TransplantRecipient)
def update_patient(patient_id: int, updated_patient: TransplantRecipientUpdate):
    for patient in all_patients:
        if patient.patient_id == patient_id:
            allowed_fields = updated_patient.dict()
            for field, value in allowed_fields.items():
                if field != "patient_id":
                    setattr(patient, field, value)
            return patient
    raise HTTPException(404, detail='Patient not found')

@api.delete('/patients/{patient_id}', response_model=TransplantRecipient)
def delete_patient(patient_id: int):
    for index, patient in enumerate(all_patients):
        if patient.patient_id == patient_id:
            deleted_patient = all_patients.pop(index)
            return deleted_patient
    raise HTTPException(404, detail='Patient not found')
