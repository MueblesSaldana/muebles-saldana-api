from app.api_v1.api import api_router as router
from app.api_v1.home.schema import Images
from app.core.handlers import convert_base_img, convert_bytes
from app.core.jwt import JWTBearer
from fastapi import Depends
import sys, cloudinary.uploader
from app.db.database import db  
from app.api_v1.home.model import HomeEntity
from bson import ObjectId

@router.post('/home/images', status_code=201, dependencies=[Depends(JWTBearer())], tags=['Images'], summary="Create image", description="Method to create image")
def create_images(images: Images):
    try:
        for i in images.images:
            image           = convert_base_img(i['base'])
            img_size_bytes  = sys.getsizeof(image)
            img_size_mb     = convert_bytes(img_size_bytes,'m')

            url = cloudinary.uploader.upload(image, folder='home/imgs')
            __image = {
                'url': url['secure_url'], 
                'id': url['public_id']
            }

            db.home.insert_one(__image).inserted_id

        return "Imagenes cargadas"
    except Exception as err:
        print(err)

@router.get('/home/images', status_code=200, tags=['Images'], summary="Get images", description="Method to get images")
def get_images():
    try:
        return HomeEntity().get_entitys(db.home.find())
    except Exception as err:
        print(err)


@router.delete('/home/images/{id}', status_code=201, dependencies=[Depends(JWTBearer())], tags=['Images'], summary="Delete image", description="Method to delete image")
def get_images(id: str, name: str):
    try:
        cloudinary.uploader.destroy(name)
        db.home.find_one_and_delete({'_id': ObjectId(id)})
        return 'Imagen eliminada'
    except Exception as err:
        print(err)
