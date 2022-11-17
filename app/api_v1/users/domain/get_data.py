from app.core.errors import response as errors
from app.api_v1.users.dao import users_dao
from app.api_v1.users.dto import Dto


class GetData:

    def execute(self, token: str):
        try:
            user        = users_dao.get_user_by_token(token)
            response    = Dto()
            return response.response_data(user)
        except Exception as err:
            print('users/Domain/execute: ', err)
            return errors["ERROR_SERVER"]
