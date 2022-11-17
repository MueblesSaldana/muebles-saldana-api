from app.api_v1.sub_categories.schemas import SubCategoryCreate
from app.db.database import db
from app.api_v1.categories.dao import CategoriesDao
from bson import ObjectId
from fastapi.responses import JSONResponse

class Dao:

    __sub_category = db.sub_categories

    def create(self, id_category: str, sub_category: SubCategoryCreate):
        try:
            category                        = CategoriesDao().get_one(id_category)
            if category is None:
                return JSONResponse(content={"message": "La categoria no existe", "data": None}, status_code=404)
                
            sub_category                    = dict(sub_category)
            sub_category['category_id']     = id_category
            sub_category['category_name']   = category['name']
            sub                             = self.__sub_category.insert_one(sub_category).inserted_id
            sub                             = self.__sub_category.find_one({'_id': sub})
            return sub
        except Exception as err:
            print('Dao error: ', err)
    
    def get_all(self):
        try:
            return self.__sub_category.find()
        except Exception as err:
            print('Dao error: ', err)
        
    def get_one_by_id(self, id: str):
        try:
            return self.__sub_category.find_one({'_id': ObjectId(id)})
        except Exception as err:
            print('Dao error: ', err)

    def get_one_by_name(self, name: str):
        try:
            return self.__sub_category.find_one({'name': name})
        except Exception as err:
            print('Dao error: ', err)

    def get_all_by_category_id(self, id: str):
        try:
            return self.__sub_category.find({'category_id': id})
        except Exception as err:
            print('Dao error: ', err)

    def update(self, id: str, sub_category: SubCategoryCreate):
        try:
            sub_category    = dict(sub_category)
            self.__sub_category.find_one_and_update({'_id': ObjectId(id)}, {'$set': sub_category})
            return self.__sub_category.find_one({'_id': ObjectId(id)})
        except Exception as err:
            print('Dao error: ', err)

    def delete(self, id: str):
        try:
            return self.__sub_category.find_one_and_delete({'_id': ObjectId(id)})
        except Exception as err:
            print('Dao error: ', err)