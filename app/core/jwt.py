from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.api_v1.auth.domain.verify_token import VerifyJwt

class JWTBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        serviceAuth = VerifyJwt()
        if credentials is None:
            raise HTTPException(status_code=403, detail='ERROR_INVALID_AUTORIZATION')
        
        if not credentials.scheme == "Bearer":
            raise HTTPException(status_code=403, detail='ERROR_INVALID_AUTHENTICATION')
        
        if not serviceAuth.execute(credentials.credentials):
            raise HTTPException(status_code=403, detail='USER_NOT_FOUND')

        return credentials.credentials
            