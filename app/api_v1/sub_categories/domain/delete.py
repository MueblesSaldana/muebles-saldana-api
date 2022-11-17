from app.api_v1.sub_categories.dao import Dao
from fastapi.responses import JSONResponse
from app.core.errors import response as errors

class Delete:
    def execute(self, id: str):
        try:
            sub = Dao().delete(id)
            if sub is None:
                return JSONResponse(content={"message": "La sub categoria no existe", "data": None}, status_code=404)
        
            return {
                "message": 'Sub categoria elimanda con exito',
                "data":     None
            }
        except Exception as err:
            print('Domain/delete/execute: ', err)
            return errors["ERROR_SERVER"]