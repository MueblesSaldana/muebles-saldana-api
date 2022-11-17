from app.api_v1.api import api_router as router
from app.api_v1.users.controller import Controller
from fastapi import status, Depends
from app.core.jwt import JWTBearer

from app.api_v1.users.schemas import CreateUser

@router.post('/user', dependencies=[Depends(JWTBearer())], tags=['Users'], summary="Create user", description="Method to create user", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser):
    controller = Controller()
    return controller.create_user(user)

@router.delete('/user/{id}', dependencies=[Depends(JWTBearer())], tags=['Users'], summary="Delete user", description="Method to delete user", status_code=status.HTTP_201_CREATED)
def delete_user(id: str):
    controller = Controller()
    return controller.delete_user(id)


@router.get('/users', dependencies=[Depends(JWTBearer())], tags=['Users'], summary="Get all users", description="Method to get all users", status_code=status.HTTP_200_OK)
def get_all():
    controller = Controller()
    return controller.get_all()

