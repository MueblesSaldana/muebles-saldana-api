from app.core.errors import response as errors
from app.api_v1.users.dao import users_dao
from app.api_v1.users.dto import Dto
from app.api_v1.users.model import UsersEntity


class GetAll:

    def execute(self):
        try:
            users        = users_dao.get_users()
            return {
                'message': 'Usuarios obtenidos con exito',
                'data':     UsersEntity().users_entity(users)
            }
        except Exception as err:
            print('users/Domain/execute: ', err)
            return errors["ERROR_SERVER"]
