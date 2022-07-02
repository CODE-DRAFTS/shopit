from fastapi import APIRouter, Depends, HTTPException, status, Response
from ..schema import CreateReview, UpdateReview, CreateReviewResponse
from ..auth import get_current_user
from sqlalchemy.orm import Session
from ..database import get_db
from .. import model
from datetime import date


router = APIRouter(
    prefix='/api/v1/review'
)


@router.post('/', response_model=CreateReviewResponse)
def create_review(review: CreateReview, user_id: str=Depends(get_current_user), db: Session=Depends(get_db)):
    #TODO check if user bought the product first
    review.user_id = user_id
    review.date =date.today()

    new_review = model.Review( **review.dict() )
    db.add( new_review) #insert review into db 
    db.commit()
    db.refresh(new_review )
    return new_review

@router.get('/' )
async def get_all_reviews(user_id: str=Depends(get_current_user), db: Session=Depends(get_db)):
    review =db.query(model.Review).filter(model.Review.user_id == user_id).all()
    return review

@router.get('/{review_id}')
async def get_single_review(review_id:int, user_id: str=Depends(get_current_user), db: Session=Depends(get_db) ):
    review = db.query(model.Review).filter( model.Review.id == review_id)
    review = review.first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'review with id {review_id} does not exist')
    if review.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not authorized to perform requested action')
    return review

@router.put('/{review_id}', status_code=status.HTTP_201_CREATED)
async def update_review(review_id:int, update_review:UpdateReview ,user_id: str=Depends(get_current_user), db: Session=Depends(get_db) ):
    review_query = db.query(model.Review).filter( model.Review.id == review_id)
    review = review_query.first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {review_id} does not exist')
    if review.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail='not authorized to perform requested action')
    review_query.update( update_review.dict(), synchronize_session=False)
    db.commit()
    return review_query.first()

@router.delete('/{review_id}')
async def delete_review( review_id: int, user_id: str=Depends(get_current_user), db: Session=Depends(get_db)):
    review = db.query(model.Review).filter(model.Review.id == review_id)
    if not review.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='review with id ' +str(review_id) +' not found')
    if review.first().user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not authorized to perform requested action')
    review.delete(synchronize_session=False)
    db.commit()
    return Response( status_code=status.HTTP_204_NO_CONTENT)

@router.get('/product/{product_id}' )
async def get_product_reviews(product_id: int, db: Session=Depends(get_db)):
    product_review = db.query(model.Review).filter(model.Review.product_id == product_id).all()
    if not product_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product with id ' +str(product_id) +' was not found')
    return product_review


