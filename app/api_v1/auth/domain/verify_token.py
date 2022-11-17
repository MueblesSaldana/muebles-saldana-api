from app.core.token import Token
from fastapi.responses import JSONResponse
from app.api_v1.users.dao import UsersDao
from app.api_v1.users.model import UsersEntity

class VerifyJwt:

    def execute(self, jwtoken: str):
        try:
            payload =   Token().decodeJWT(jwtoken)
            
            if not payload:
                print('err')
                return JSONResponse(content={'message': 'Token invalido', 'data': None}, status_code=400)

            user         = Token().userGetToken(token=jwtoken)
            __user       = UsersDao().get_user(user['id_user'])

            return {
                'message': 'Informacion del usuario',
                'data':     UsersEntity().user_entity(__user)
            }

        except Exception as err:
            print(err)
