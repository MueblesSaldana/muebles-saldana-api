from app.api_v1.sub_categories.schemas import SubCategoryCreate
from app.api_v1.sub_categories.dao import Dao
from app.api_v1.sub_categories.model import SubCategoryEntity
from fastapi.responses import JSONResponse


class Create:
    def execute(self, id_category: str, sub_category: SubCategoryCreate):
        try:
            __sub = Dao().get_one_by_name(sub_category.name)

            if __sub:
                return JSONResponse(content='La sub categoria ya existe', status_code=400)
            
            sub = Dao().create(id_category, sub_category)

            if type(sub) is JSONResponse:
                return sub

            return {
                "message": 'Sub categoria creada con exito',
                "data":     SubCategoryEntity().get_entity(sub)
            }
        except Exception as err:
            print('Create subcategory error: ', err)