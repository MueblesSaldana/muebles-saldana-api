from app.api_v1.sub_categories.model import SubCategoryEntity
from app.api_v1.sub_categories.dao import Dao
from fastapi.responses import JSONResponse

class GetAllByCategoryId:
    def execute(self, id: str):
        try:
            subs = Dao().get_all_by_category_id(id)
            if subs is None:
                return JSONResponse(content={"message": "La categoria no existe", "data": None}, status_code=404)
                
            return {
                "message": 'Sub categorias obtenidas con exito',
                "data":     SubCategoryEntity().get_entitys(subs)
            }
        except Exception as err:
            print('Get all subcategory by category id error: ', err)