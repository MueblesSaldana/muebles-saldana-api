from app.core.errors import response as errors
from app.api_v1.users.schemas import CreateUser
from bson import ObjectId

from app.db.database import db

class UsersDao:
    def create_user(self, user: CreateUser, password):
        try:
            data                = dict(user)
            data['password']    = password
            user                = db.users.insert_one(data).inserted_id
            user                = db.users.find_one({'_id': user})
            return user
        except Exception as err:
            print('Dao/create_user: ', err)
            return errors["ERROR_SERVER"]

    def get_user(self, id: str):
        try:
            user =  db.users.find_one({'_id': ObjectId(id)})
            return user
        except Exception as err:
            print('Dao/get_user: ', err)
            return errors["ERROR_SERVER"]
    def get_user_by_email(self, email: str):
        try:
            user =  db.users.find_one({'email': email})
            return user
        except Exception as err:
            print('Dao/get_user: ', err)
            return errors["ERROR_SERVER"]

    def get_users(self):
        try:
            user =  db.users.find()
            return user
        except Exception as err:
            print('Dao/get_users: ', err)
            return errors["ERROR_SERVER"]

    def delete_user(self, id):
        try:
            user = db.users.find_one_and_delete({'_id': ObjectId(id)})
            return user
        except Exception as err:
            print('Dao/get_users: ', err)
            return errors["ERROR_SERVER"]



users_dao = UsersDao()