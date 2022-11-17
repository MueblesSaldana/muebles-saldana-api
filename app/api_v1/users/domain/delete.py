
from app.core.errors import response as errors
from app.api_v1.users.dao import users_dao
from app.api_v1.users.model import UsersEntity
from fastapi.responses import JSONResponse


class Delete:

    def execute(self, id: str):
        try:
            user        = users_dao.delete_user(id)

            if user is None:
                return JSONResponse(content={"message": "El usuario no existe", "data": None}, status_code=404)
            
            user = UsersEntity().user_entity(user)
            return {
                "message": 'Usuario eliminado con exito',
                "data":     None
            }
        except Exception as err:
            print('users/Domain/execute: ', err)
            return errors["ERROR_SERVER"]
