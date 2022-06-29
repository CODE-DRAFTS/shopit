from fastapi import APIRouter, Depends
from ..schema import Review, UpdateReview
from ..auth import get_current_user

router = APIRouter(
    prefix='/api/v1/review'
)


@router.post('/')
def create_review(review: Review, user_id: str=Depends(get_current_user)):
    #check if user bought the product first
    #TODO insert review into db
    return {'created a review '}

@router.get('/')
async def get_all_reviews(user_id: str=Depends(get_current_user)):
    #TODO fetch all users product reviews
    return {'all my reviews'}

@router.get('/{review_id}')
async def get_single_review(user_id: str=Depends(get_current_user)):
    #TODO fetch single review
    return {'single review'}

@router.put('/{review_id}')
async def update_review(review:UpdateReview ,user_id: str=Depends(get_current_user)):
    #TODO update a review
    return {'updated review'}

@router.delete('/{review_id}')
async def delete_review(user_id: str=Depends(get_current_user)):
    #TODO delete review
    return {'deleted  review'}


