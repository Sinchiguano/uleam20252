from pydantic import BaseModel, Field, EmailStr
from typing import Optional 



class StudentIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)

class StudentOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    
    

    

    