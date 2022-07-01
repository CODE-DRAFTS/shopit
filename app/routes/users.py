from fastapi import APIRouter, Depends, Response, HTTPException, status, BackgroundTasks
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..schema import CreateUser, UserOut, UserDetails
from ..auth import create_access_token, get_current_user
from sqlalchemy.orm import Session
from ..database import get_db
from .. import model, utils, mails



router = APIRouter(
    prefix='/api/v1/user',
    tags=['USERS']
)


@router.post("/login",  status_code=status.HTTP_200_OK)
async def login(response: Response, db: Session=Depends(get_db), user_credentials: OAuth2PasswordRequestForm=Depends()  ):
    user = db.query( model.User).filter( model.User.email== user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= user_credentials.username +'email does not exists')
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='wrong password')
    
    access_token = create_access_token( data={"user_id": user.user_id})
    response.set_cookie(key='Authorization', value='Bearer ' +str(access_token))
    return { "access_token": access_token, "token_type": "bearer"}
    

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserOut )
async def create_user(user: CreateUser, background_tasks: BackgroundTasks, db: Session=Depends(get_db) ):
    user_email = db.query(model.User).filter( model.User.email== user.email).first()
    if user_email != None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='email ' +user.email +' already exists')

    user.password = utils.hash_function(user.password)
    new_user = model.User( **user.dict() )
    db.add( new_user)  #insert user into db
    db.commit()
    db.refresh(new_user)
    
    background_tasks.add_task( mails.new_user, user.email ) #send email to user
    return new_user

@router.get('/', response_model=UserDetails)
async def get_user(user_id: str=Depends(get_current_user),  db: Session=Depends(get_db)):
    user= db.query( model.User).filter( model.User.user_id == user_id).first()
    return user
