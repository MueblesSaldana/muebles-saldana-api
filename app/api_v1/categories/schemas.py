from uuid import UUID
from pydantic import BaseModel

class CreateCategory(BaseModel):
    name: str


class Category(BaseModel):
    id:     str
    name:   str