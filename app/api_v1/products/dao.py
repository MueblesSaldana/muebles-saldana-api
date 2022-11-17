from app.api_v1.products.schemas.create import CreateProduct, UpdateProduct
from app.api_v1.sub_categories.dao import Dao as SubCategoryDao
from app.api_v1.categories.dao import CategoriesDao
from app.db.database import db
from fastapi.responses import JSONResponse
from bson import ObjectId
from app.api_v1.products.model import ProductsEntity

class Dao:

    __products = db.products

    def create(self, product: CreateProduct):
        
        try:
            category = CategoriesDao().get_one(product.category_id)
            sub_category = SubCategoryDao().get_one_by_id(product.sub_category_id)
            name = sub_category['name']
            if category is None:
                return JSONResponse(content={"message": "La categoria no existe", "data": None}, status_code=404)
            if sub_category is None:
                return JSONResponse(content={"message": "La sub categoria no existe", "data": None}, status_code=404)

            __product                       = dict(product)
            __product['category_name']      = category['name']
            __product['sub_category_name']  = name
            response                        = self.__products.insert_one(__product).inserted_id
            response                        = self.__products.find_one({'_id': response}) 
            return response
        except Exception as err:
            print('Create DAO: ', err)

    def get_all(self):
        return self.__products.find()


    def get_one_by_id(self, id: str):
        if self.__products.find_one({'_id': ObjectId(id)}) is None:
            return JSONResponse(content='Producto no encontrado', status_code=404)
        return ProductsEntity().get_entity(self.__products.find_one({'_id': ObjectId(id)}))

    def get_one_by_name(self, name: str):
        return self.__products.find_one({'name': name})

    def get_all_by_category_id(self, id: str):
        return self.__products.find({'category_id': id})

    def get_all_by_sub_category_id(self, id: str):
        return self.__products.find({'sub_category_id': id})

    def delete(self, id: str):
        if self.__products.find_one({'_id': ObjectId(id)}) is None:
            return JSONResponse(content='Producto no encontrado', status_code=404)
        return self.__products.find_one_and_delete({'_id': ObjectId(id)})

    def update(self, product: UpdateProduct, id):
        product_one = self.get_one_by_id(id)
        __product    = dict(product)
        __product['old_price'] = product_one['price']
        self.__products.find_one_and_update({'_id': ObjectId(id)}, {'$set': __product})
        return self.__products.find_one({'_id': ObjectId(id)})