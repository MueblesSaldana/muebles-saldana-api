from app.api_v1.users.schemas import CreateUser
from app.core.errors import response as errors
from app.api_v1.users.dao import users_dao
from app.api_v1.users.dto import Dto
from passlib.hash import pbkdf2_sha256
from app.api_v1.users.model import UsersEntity
from fastapi.responses import JSONResponse

class Create:

    def execute(self, user: CreateUser):
        try:
            __user = users_dao.get_user_by_email(user.email)
            if __user:
                return JSONResponse(content='El Usuario ya existe', status_code=400)
            password    = pbkdf2_sha256.hash(user.password)
            user        = users_dao.create_user(user, password)

            user        = UsersEntity().user_entity(user)

            response    = Dto()
            return response.response(user)
        except Exception as err:
            print('users/Domain/execute: ', err)
            return errors["ERROR_SERVER"]
