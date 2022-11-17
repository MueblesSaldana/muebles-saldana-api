from app.api_v1.products.schemas.create import CreateProduct, UpdateProduct
from app.api_v1.products.domain.create import Create
from app.api_v1.products.domain.get_all import GetAll
from app.api_v1.products.dao import Dao
from fastapi.responses import JSONResponse
import cloudinary.uploader


class Controller:

    def create(self, product: CreateProduct):
        try:
            return Create().execute(product)
        except Exception as err:
            print('Error in controller: ', err)

    def get_all(self, category_id, sub_category_id):
        try:
            return GetAll().execute(category_id, sub_category_id)
        except Exception as err:
            print('Error in controller: ', err)


    def get_one(self, id: str):
            try:
                product = Dao().get_one_by_id(id)

                if type(product) == JSONResponse:
                    return product

                if product:
                    return {
                        'data': product
                    }

                return JSONResponse(content='Producto no existente', status_code=404)
            except Exception as err:
                print('Error in controller: ', err)

    def delete(self, id: str):
            try:
                images = Dao().get_one_by_id(id)
                for img in images['images']:
                    cloudinary.uploader.destroy(img['id'])
                Dao().delete(id)
                if type(Dao().delete(id)) == JSONResponse:
                    return Dao().delete(id)
                return {
                    'message': 'Producto Eliminado'
                }
            except Exception as err:
                print('Error in controller: ', err)

    def update(self, id: str, update_data: UpdateProduct):
            try:
                up = Dao().update(update_data, id)
                if type(up) == JSONResponse:
                    return up
                return {
                    'message': 'actualizado con exito'
                }
            except Exception as err:
                print('Error in controller: ', err)

