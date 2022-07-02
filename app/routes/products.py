from fastapi import APIRouter,Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import model

router = APIRouter(
    prefix='/api/v1/product'
)

@router.get('/categories')
async def get_all_categories( db: Session=Depends(get_db)):
    categories =db.query(model.Category).all()
    return categories

@router.get('/category/{category_id}')
async def get_category_products(category_id:int, db: Session=Depends(get_db)):
    products = db.query(model.Product).filter(model.Product.category_id == category_id).all()
    return products

@router.get('/popular')
async def get_popular():
    #TODO fetch popular products from db
    return {'popular products'}

@router.get('/search')
async def search_products(product: str, db: Session=Depends(get_db) ):
    #TODO reseach on better logic to perform search endpoints
    return f'searched products {product}'

@router.get('/{product_id}')
async def get_single_product(product_id: str, db: Session=Depends(get_db) ):
    #TODO fetch product from db
    product = db.query(model.Product).filter(model.Product.product_id == product_id)
    product = product.first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id {product_id} was not found')
    return product

