from typing import List, Optional
from pydantic import BaseModel

class Images(BaseModel):
    img: str

class CreateProduct(BaseModel):
    name            : str
    description     : str
    category_id     : str
    sub_category_id : str
    price           : float
    old_price       : Optional[float]
    quantity        : int
    images          : List
    images_item     : List  



class UpdateProduct(BaseModel):
    price           : float
    quantity        : int


