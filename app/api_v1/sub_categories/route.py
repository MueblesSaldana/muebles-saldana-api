from app.api_v1.api import api_router as router
from app.api_v1.sub_categories.controller import Controller
from app.api_v1.sub_categories.schemas import SubCategoryCreate
from fastapi import status, Depends
from app.core.jwt import JWTBearer

@router.post('/categories/{id_category}/sub_category', dependencies=[Depends(JWTBearer())], tags=['Sub Categories'], summary="Create subcategory", description="Method to create subcategory", status_code=status.HTTP_201_CREATED)
def create(id_category: str, sub_category: SubCategoryCreate):
    return Controller().create_sub_category(id_category, sub_category)

@router.get('/sub_category', tags=['Sub Categories'], summary="Get all subcategories", description="Method to get all subcategories", status_code=status.HTTP_200_OK)
def get_all(category_id: str = None):
    return Controller().get_all(category_id)

@router.delete('/sub_category/{id}', dependencies=[Depends(JWTBearer())], tags=['Sub Categories'], summary="Delete subcategory", description="Method to detele subcategory", status_code=status.HTTP_201_CREATED)
def delete(id: str):
    return Controller().delete(id)

@router.get('/sub_category/{id}', dependencies=[Depends(JWTBearer())], tags=['Sub Categories'], summary="Get subcategory", description="Method to get subcategory", status_code=status.HTTP_200_OK)
def get_one(id: str):
    return Controller().get_one(id)


    

    