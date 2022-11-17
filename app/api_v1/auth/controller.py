from app.api_v1.auth.domain.verify_token import VerifyJwt
from app.api_v1.auth.schema import Login
from app.api_v1.auth.domain.login import LoginUser


class Controller:

    def login(self, user_data: Login):
        try:
            return LoginUser().execute(user_data)
        except Exception as err:
            print(err)


    def token_verification(self, token: str):
        try:
            return VerifyJwt().execute(token)
        except Exception as err:
            print("ERROR GENERAL")
            print("TIPO", type(err))
            print("controller/token_verification", err)