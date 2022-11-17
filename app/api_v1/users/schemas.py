from typing import Optional
from pydantic import BaseModel

class CreateUser(BaseModel):
    name:       str
    lastname:   str
    user_name:  str
    email:      str
    password:   str


class UserResponse(BaseModel):
    message:    str
    data:       Optional[None]