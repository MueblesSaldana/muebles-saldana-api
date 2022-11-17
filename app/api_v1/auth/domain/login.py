from app.api_v1.auth.schema import Login
from app.core.token import Token
from app.api_v1.auth.dao import Dao
from app.api_v1.users.model import UsersEntity
from passlib.hash import pbkdf2_sha256
from fastapi.responses import JSONResponse


class LoginUser:

    def execute(self, user_data: Login):
        try:
            user        = Dao().get_user_by_email(user_data.email)
            if user is None:
                return JSONResponse(content={"message": "Usuario no encontrado", "data": None}, status_code=404)

            user        = UsersEntity().user_entity(user)
            user_id     = user['id']

            if not pbkdf2_sha256.verify(user_data.password, user['password']):
                return JSONResponse(content={'message': 'Password incorrecto', 'data': None}, status_code=400)

            token       = Token().createToken(user_id)

            return {
                'message': 'Usuario loggeado exitosamente',
                'access_token': token 
            }
        except Exception as err:
            print(err)