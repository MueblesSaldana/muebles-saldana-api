from app.api_v1.users.schemas import CreateUser
from app.core.errors import response as errors
from app.api_v1.users.domain.create import Create
from app.api_v1.users.domain.get_data import GetData
from app.api_v1.users.domain.delete import Delete
from app.api_v1.users.domain.get_all import GetAll

class Controller:

    def create_user(self, user: CreateUser):
        try:
            category = Create()
            return category.execute(user)
        except Exception as err:
            print('Controller/create_category: ', err)
            return errors["ERROR_CREATE_USER"]

    def get_data(self, token: str):
        try:
            category = GetData()
            return category.execute(token)
        except Exception as err:
            print('Controller/get_data: ', err)
            return errors["ERROR_CREATE_USER"]

    def delete_user(self, id: str):
        try:
            return Delete().execute(id)
        except Exception as err:
            print('Controller/delete_user: ', err)
            return errors["ERROR_CREATE_USER"]

    def get_all(self):
        try:
            return GetAll().execute()
        except Exception as err:
            print('Controller/get_all: ', err)
            return errors["ERROR_CREATE_USER"]