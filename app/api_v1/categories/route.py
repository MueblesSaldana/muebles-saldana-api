from app.api_v1.api import api_router as router
from app.api_v1.categories.controller import Controller
from app.api_v1.categories.schemas import CreateCategory
from fastapi import status, Depends
from app.core.jwt import JWTBearer

@router.post('/categories', dependencies=[Depends(JWTBearer())], tags=['Categories'], summary="Create category", description="Method to create category", status_code=status.HTTP_201_CREATED)
def create_category(data_category: CreateCategory):
    controller = Controller()
    return controller.create_category(data_category)


@router.get('/categories', tags=['Categories'], summary="Get all categories", description="Method to get all categories", status_code=status.HTTP_200_OK)
def get_all_categories():
    controller = Controller()
    return controller.get_all()


@router.get('/categories/{id}', tags=['Categories'], summary="Get one category", description="Method to get category", status_code=status.HTTP_200_OK)
def get_all_categories(id: str):
    controller = Controller()
    return controller.get_one(id)

@router.put('/categories/{id}', dependencies=[Depends(JWTBearer())], tags=['Categories'], summary="Update category", description="Method to update category", status_code=status.HTTP_201_CREATED)
def update(id: str, data_category: CreateCategory):
    controller = Controller()
    return controller.update(id, data_category)

@router.delete('/categories/{id}', dependencies=[Depends(JWTBearer())], tags=['Categories'], summary="Delete category", description="Method to delete category", status_code=status.HTTP_201_CREATED)
def delete(id: str):
    controller = Controller()
    return controller.delete(id)