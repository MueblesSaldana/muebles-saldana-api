from app.api_v1.sub_categories.schemas import SubCategoryCreate
from app.api_v1.sub_categories.domain.exports import Create, GetAll, GetAllByCategoryId, Delete,GetOne

class Controller:

    def create_sub_category(self, id_category: str, sub_category: SubCategoryCreate):
        try:
            return Create().execute(id_category, sub_category)
        except Exception as err:
            print('Error in controller: ', err)

    def get_all(self, category_id: str):
        try:
            if category_id:
                return GetAllByCategoryId().execute(category_id)

            return GetAll().execute()
        except Exception as err:
            print('Error in controller: ', err)

    def delete(self, id: str):
            try:
                return Delete().execute(id)
            except Exception as err:
                print('Error in controller: ', err)

    def get_one(self, id: str):
            try:
                return GetOne().execute(id)
            except Exception as err:
                print('Error in controller: ', err)
