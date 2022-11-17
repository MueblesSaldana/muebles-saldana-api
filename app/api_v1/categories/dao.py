from bson import ObjectId
from app.api_v1.categories.schemas import CreateCategory
from app.core.errors import response as errors
from app.api_v1.categories.models.category_entity import CategoryEntity

from app.db.database import db

class CategoriesDao:

    def create_category(self, data_category: CreateCategory):
        try:
            category = db.categories.insert_one(dict(data_category)).inserted_id
            category = db.categories.find_one({'_id': category})
            return CategoryEntity().get_entity(category)
        except Exception as err:
            print('Dao/create_category: ', err)
            return errors["ERROR_SERVER"]


    def get_all(self):
        try:
            return CategoryEntity().get_entitys(db.categories.find())
        except Exception as err:
            print('Dao/get_all: ', err)
            return errors["ERROR_SERVER"]

    def get_one(self, id: str):
        try:
            category = db.categories.find_one({'_id': ObjectId(id)})
            return category
        except Exception as err:
            print('Dao/get_one: ', err)
            return errors["ERROR_SERVER"]

    def get_by_name(self, name: str):
        try:
            category = db.categories.find_one({'name': name})
            return category
        except Exception as err:
            print('Dao/get_one_by_name: ', err)
            return errors["ERROR_SERVER"]

    def delete(self, id: str):
        try:
            category = db.categories.find_one_and_delete({'_id': ObjectId(id)})
            return category
        except Exception as err:
            print('Dao/delete: ', err)
            return errors["ERROR_SERVER"]

    def update(self, id: str, data_category: CreateCategory):
        try:
            category = db.categories.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(data_category)})
            return category
        except Exception as err:
            print('Dao/update: ', err)
            return errors["ERROR_SERVER"]

category_dao = CategoriesDao()