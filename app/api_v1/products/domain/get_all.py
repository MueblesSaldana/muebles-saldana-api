from app.api_v1.products.dao import Dao
from app.api_v1.products.model import ProductsEntity
from fastapi.responses import JSONResponse


class GetAll:
    def execute(self, category_id, sub_category_id):
        try:

            products = Dao().get_all()

            if category_id:
                products = Dao().get_all_by_category_id(category_id)

            if sub_category_id:
                products = Dao().get_all_by_sub_category_id(sub_category_id)



            if type(products) is JSONResponse:
                return products

            response = ProductsEntity().get_entitys(products)

            return {
                'message': 'Productos obtendidos con exito',
                'data':     response
            }

        except Exception as err:
            print('Get all: ', err)