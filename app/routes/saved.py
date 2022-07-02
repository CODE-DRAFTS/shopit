from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..schema import SavedItem
from ..auth import get_current_user
from sqlalchemy.orm import Session
from ..database import get_db
from .. import model

router = APIRouter(
    prefix='/api/v1/save'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def save_product(item:SavedItem,  user_id: str=Depends(get_current_user), db: Session=Depends(get_db) ):
    item.user_id = user_id
    new_item = model.Saved( **item.dict() )
    db.add( new_item)  
    db.commit()
    db.refresh(new_item )
    return new_item

@router.get('/')
async def get_saved_items(user_id: str=Depends(get_current_user), db: Session=Depends(get_db) ):
    item =db.query(model.Saved).filter(model.Saved.user_id == user_id).all()
    return item

@router.get('/{item_id}')
async def get_item(item_id:int, user_id: str=Depends(get_current_user), db: Session=Depends(get_db)):
    item =db.query(model.Saved).filter(model.Saved.id == item_id)
    item = item.first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'saved with id {item_id} does not exist')
    if item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not authorized to perform requested action')
    return item


@router.delete('/{item_id}')
async def delete_saved_item(item_id:int, user_id: str=Depends(get_current_user), db: Session=Depends(get_db)):
    item =db.query(model.Saved).filter(model.Saved.id == item_id)
    if not item.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'item with id {item_id} not found')
    if item.first().user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not authorized to perform requested action')
    item.delete(synchronize_session=False)
    db.commit()
    return Response( status_code=status.HTTP_204_NO_CONTENT)
