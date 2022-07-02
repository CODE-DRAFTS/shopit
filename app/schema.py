from pydantic import BaseModel, EmailStr, PastDate, validator, ValidationError
from fastapi import HTTPException, status
from typing import Optional
from datetime import date

#pydantic models
class CreateUser(BaseModel):
    email: EmailStr
    password: str
    name: str
    dob: PastDate
    phone: str
    address: str
    @validator('email')
    def len_email(cls, email):
        if len(email) <100:          return email
        else:raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='email too long')

class UserOut(BaseModel):
    user_id: int
    email: str
    class Config:
        orm_mode= True

class UserDetails(BaseModel):
    user_id: int
    email: EmailStr
    name: str
    dob: PastDate
    phone: str
    address: str
    class Config:
        orm_mode= True




class Order(BaseModel):
    items: list

class CreateReview(BaseModel):
    user_id: Optional[int] =None
    product_id: int   #product_id
    review: str
    date: Optional[date]

class CreateReviewResponse(BaseModel):
    review: str
    id: int
    user_id: int
    date: date
    product_id: int
    class Config:
        orm_mode= True
    

class UpdateReview(BaseModel):
    review: str


class SavedItem(BaseModel):
    product_id: int
    user_id: Optional[int]=None


