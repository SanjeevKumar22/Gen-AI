from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'vik'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student')


new_std = {"age":'32','email':'abc@gmail.com','cgpa':1} #coierce
student = Student(**new_std)
print(student.model_dump())