from app.db.database import db

class Dao:
    def get_user_by_email(self, email: str):
        try:
            user = db.users.find_one({'email': email})
            return user
        except Exception as err:
            print('Dao/get_user_by_email: ', err)
