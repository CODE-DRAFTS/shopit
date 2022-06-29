from pydantic import BaseModel, EmailStr, PastDate


class User(BaseModel):
    email: EmailStr
    password: str
    name: str
    dob: str #TODO: validate input to past date
    phone: str
    address: str

class Order(BaseModel):
    items: list

class Review(BaseModel):
    review: str
    product: int   #product_id

class UpdateReview(BaseModel):
    review: str

class SavedItem(BaseModel):
    product: int


