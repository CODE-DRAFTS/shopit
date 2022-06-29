from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..schema import User
from ..auth import create_access_token, get_current_user

router = APIRouter(
    prefix='/api/v1/user'
)


@router.post("/login" )
async def login(user: OAuth2PasswordRequestForm=Depends() ):
    #TODO: if email exists and return password, user_id
    #TODO:hash attempted password and match with actual pasword
    #create access token
    access_token = create_access_token( data={"user_id": "user id"}) #TODO : embed user_id here
    #TODO:set cookie header
    return { "access_token": access_token, "token_type": "bearer"}
    

@router.post('/create')
async def create_user(user: User):
    #insert user into db
    #initiate background task to send email to user
    return user

@router.get('/')
async def get_user(user_id: str=Depends(get_current_user)):
    #TODO get user details except password
    return user_id
