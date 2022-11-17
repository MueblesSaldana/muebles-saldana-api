from app.api_v1.api import api_router as router
from fastapi import status, Depends
from app.core.jwt import JWTBearer
from app.api_v1.products.schemas.create import CreateProduct, UpdateProduct
from app.api_v1.products.controller import Controller

@router.post('/products', dependencies=[Depends(JWTBearer())], tags=['Products'], summary="Create product", description="Method to create product", status_code=status.HTTP_201_CREATED)
def create(product: CreateProduct):
    return Controller().create(product)

@router.get('/products', tags=['Products'], summary="Get products", description="Method to get products", status_code=status.HTTP_200_OK)
def get_all(category_id: str = None, sub_category_id: str = None):
    return Controller().get_all(category_id, sub_category_id)

@router.get('/products/{id}', tags=['Products'], summary="Get product", description="Method to get product", status_code=status.HTTP_200_OK)
def get_one(id: str):
    return Controller().get_one(id)

@router.put('/products/{id}', dependencies=[Depends(JWTBearer())], tags=['Products'], summary="Update product", description="Method to update product", status_code=status.HTTP_201_CREATED)
def update(id: str, update_data: UpdateProduct):
    return Controller().update(id, update_data)

@router.delete('/products/{id}', dependencies=[Depends(JWTBearer())], tags=['Products'], summary="Delete product", description="Method to delete product", status_code=status.HTTP_201_CREATED)
def delete(id: str):
    return Controller().delete(id)