from fastapi import APIRouter, Depends
from ..schema import SavedItem
from ..auth import get_current_user

router = APIRouter(
    prefix='/api/v1/save'
)


@router.post('/')
def save_product(item:SavedItem,  user_id: str=Depends(get_current_user)):
    #TODO insert saved item into db
    return {'saved an item'}

@router.get('/')
async def get_saved_items(user_id: str=Depends(get_current_user)):
    #TODO fetch all saved items
    return {'all saved items'}

@router.get('/{item_id}')
async def get_item(user_id: str=Depends(get_current_user)):
    #TODO fetch single item
    return {'single saved item'}


@router.delete('/{item_id}')
async def delete_saved_item(user_id: str=Depends(get_current_user)):
    #TODO delete saved product
    return {'deleted  saved product'}
