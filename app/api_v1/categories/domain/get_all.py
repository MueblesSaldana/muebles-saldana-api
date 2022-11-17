from app.core.errors import response as errors
from app.api_v1.categories.dao import category_dao

class GetAll:
    def execute(self):
        try:
            categories = category_dao.get_all()
            return {
                "message": 'Categorias obtenidas con exito',
                "data":     categories
            }
        except Exception as err:
            print('Domain/get_all/execute: ', err)
            return errors["ERROR_SERVER"]