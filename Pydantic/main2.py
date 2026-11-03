from pydantic import BaseModel, EmailStr, AnyHttpUrl,AnyUrl, Field
 
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=40,title='Name of the patient',description='Give the name of the patient in less than 40 chars',examples=['Nikhil','Kajal'])]
    age:int
    weight:float = Field(gt=0)
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    job:Optional[bool]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("inserted")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info={'name':'nikhil','age':22,'weight':55.4,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abs@gmail.com','phone':'123456'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)