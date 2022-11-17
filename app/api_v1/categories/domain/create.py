from app.api_v1.categories.schemas import CreateCategory
from app.core.errors import response as errors
from app.api_v1.categories.dao import category_dao

from fastapi.responses import JSONResponse

class Create:
    def execute(self, data_category: CreateCategory):
        try:
            cat = category_dao.get_by_name(data_category.name)

            if cat:
                return JSONResponse(content='La categoria ya existe', status_code=400)
            category = category_dao.create_category(data_category)
            return {
                "message": 'Categoria creada con exito',
                "data":     category
            }
        except Exception as err:
            print('Domain/execute: ', err)
            return errors["ERROR_SERVER"]