from app.api_v1.sub_categories.model import SubCategoryEntity
from app.api_v1.sub_categories.dao import Dao

class GetAll:
    def execute(self):
        try:
            subs = Dao().get_all()
            return {
                "message": 'Sub categorias obtenidas con exito',
                "data":     SubCategoryEntity().get_entitys(subs)
            }
        except Exception as err:
            print('Get all subcategory error: ', err)