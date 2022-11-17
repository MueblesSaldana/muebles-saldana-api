from app.api_v1.categories.schemas import CreateCategory
from app.core.errors import response as errors
from app.api_v1.categories.dao import category_dao
from fastapi.responses import JSONResponse
from app.api_v1.categories.models.category_entity import CategoryEntity

class Update:
    def execute(self, id: str, data_category: CreateCategory):
        try:
            category = category_dao.update(id, data_category)
            if category is None:
                return JSONResponse(content={"message": "La categoria buscada no existe", "data": None}, status_code=404)
            
            category = CategoryEntity().get_entity(category)
            return {
                "message": 'Categoria actualizada con exito',
                "data":     None
            }
        except Exception as err:
            print('Domain/get_one/execute: ', err)
            return errors["ERROR_SERVER"]