from fastapi import APIRouter, status, Depends
from ..auth import get_current_user
from ..schema import Order

router = APIRouter(
    prefix='/api/v1/order'
)

@router.post('/')
async def create_order(order:Order, user_id: str=Depends(get_current_user)):
    #TODO create a new order
    #TODO insert order into db
    return {'created order'}

@router.get('/')
async def get_all_orders( user_id: str=Depends(get_current_user)):
    #TODO fetch all user orders
    return {'all orders'}


@router.get('/{order_id}')
async def get_single_order(user_id: str=Depends(get_current_user)):
    #TODO fetch single order
    return {'single order'}