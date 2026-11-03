from pydantic import BaseModel, EmailStr, AnyHttpUrl,AnyUrl, Field, computed_field
 
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age:int
    weight:float 
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    # job:Optional[bool]

@computed_field
@property
def calculate_bmi(self) -> float:
    bmi = round(self.weight/(self.height**2),2)
    return bmi