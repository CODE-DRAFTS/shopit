from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1/product'
)

@router.get('/categories')
async def get_all_categories():
    #TODO fetch all categories info
    return {'all categories list'}

@router.get('/category/{category_id}')
async def get_category_products(category_id):
    #TODO fetch products of a particular category from db
    return {'category_products'}

@router.get('/popular')
async def get_popular():
    #TODO fetch popular products from db
    return {'popular products'}

@router.get('/search')
async def search_products(product: str):
    #TODO reseach on better logic to perform search endpoints
    return {'searched products'}

@router.get('/{product_id}')
async def get_single_product():
    #TODO fetch product from db 
    return {'single product'}


