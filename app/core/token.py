import time, json, jwt
from cryptography.fernet import Fernet
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.core.settings import settings

class Token:

    # Crea el token donde se loguea el usuario
    def createToken(self, id_user: int):
        try:
            encryptor = Fernet(settings.KEY)
            data = {}
            data['id_user'] = str(id_user)
            data = json.dumps(data)
            data_encrypt = encryptor.encrypt(data.encode())
            token_create = {
                "data": data_encrypt.decode(),
                "expires": time.time() + settings.ACCESS_TOKEN_EXPIRE_MINUTES
            }
            token = jwt.encode(token_create, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
            return token
        except Exception as err:
            print(err)

    
    # Desencripta el token  
    def decodeJWT(self, token: str):
        try:
            token           = token.replace('Bearer ', '')
            decoded_token   = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
            if decoded_token['expires'] >= time.time():
                return decoded_token
            else:
                print("core /token/decodeJWT/Expired token/EXPIRED_TOKEN")
        except:
            print("core /token/decodeJWT/Expired token/EXPIRED_TOKEN")
    # Obtiene la data del token del login
    def userGetToken(self, token: str):
        try:
            token       = self.decodeJWT(token=token)

            encryptor   = Fernet(settings.KEY)
            if 'data' in token:
                data    = encryptor.decrypt(token['data'].encode())
                data    = data.decode()
                data    = json.loads(data)
                return data
        except:
            print("core /token/decodeJWT/Expired token/EXPIRED_TOKEN")
    
    # Obtiene la data del token de la creacion del usuairo
    def user_token(self, token):
        token = self.decodeJWT(token=token)
        encryptor = Fernet(settings.KEY)
        if type(token) == JSONResponse:
            return token
        data = encryptor.decrypt(token['data'].encode())
        data = data.decode()
        data = json.loads(data)
        return data['id_user']
    
    # Verifica JWT
    def verify_jwt(self, jwtoken: str):
        try:
            try:
                payload = self.decodeJWT(jwtoken)
                print(payload)
            except:
                payload = None
    
            if payload:
                user = self.userGetToken(token=jwtoken)
                user_get = self.get_user(user_id=user['id_user'])

                response = {}
                response['user'] = {}
                response['user']['id'] = user_get.id
                return JSONResponse(status_code=200, content={'message':'Token is Valid', 'data': jsonable_encoder(response)})
            
            return JSONResponse(status_code=403, content={'message':'Token is Invalid', 'data': None})
        except Exception as err:
            print(err)


token_ = Token()