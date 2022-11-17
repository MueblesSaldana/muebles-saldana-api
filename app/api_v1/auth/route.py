from app.api_v1.api import api_router as router
from app.api_v1.auth.schema import Login
from app.api_v1.auth.controller import Controller

@router.post('/auth/login', tags=['Auth'], summary='Login of user admin', description='Method to login user', status_code=201)
def login(user_data: Login):
    return Controller().login(user_data)


@router.get("/auth/verify_token", tags=["Auth"], summary="Verfication Token", description="Verfication with token")
def verify_token(token: str):
    return Controller().token_verification(token)
