from re import U
from uuid import UUID
from app.api_v1.categories.domain.get_all import GetAll
from app.api_v1.categories.domain.delete import Delete
from app.api_v1.categories.domain.update import Update
from app.api_v1.categories.domain.get_one import GetOne
from app.api_v1.categories.schemas import CreateCategory
from app.core.errors import response as errors
from app.api_v1.categories.domain.create import Create

class Controller:
    def create_category(self, data_category: CreateCategory):
        try:
            category = Create()
            return category.execute(data_category)
        except Exception as err:
            print('Controller/create_category: ', err)
            return errors["ERROR_CREATE_CATEGORY"]


    def get_all(self):
        try:
            categories = GetAll()
            return categories.execute()
        except Exception as err:
            print('Controller/create_category: ', err)
            return errors["ERROR_GET_CATEGORY"]

    
    def get_one(self, id: str):
        try:
            categories = GetOne()
            return categories.execute(id)
        except Exception as err:
            print('Controller/create_category: ', err)
            return errors["ERROR_GET_CATEGORY"]

    def delete(self, id: str):
        try:
            return Delete().execute(id)
        except Exception as err:
            print('Controller/delete: ', err)
            return errors["ERROR_GET_CATEGORY"]

    def update(self, id: str, data_category: CreateCategory):
        try:
            return Update().execute(id, data_category)
        except Exception as err:
            print('Controller/create_category: ', err)
            return errors["ERROR_GET_CATEGORY"]