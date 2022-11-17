from app.api_v1.sub_categories.dao import Dao
from fastapi.responses import JSONResponse
from app.api_v1.sub_categories.model import SubCategoryEntity
from app.core.errors import response as errors


class GetOne:
    def execute(self, id: str):
        try:
            sub = Dao().get_one_by_id(id)
            if sub is None:
                return JSONResponse(content={"message": "La sub categoria no existe", "data": None}, status_code=404)
            
            sub = SubCategoryEntity().get_entity(sub)
            return {
                "message": 'Sub categoria obtenida con exito',
                "data":     sub
            }
        except Exception as err:
            print('Domain/get_one/execute: ', err)
            return errors["ERROR_SERVER"]