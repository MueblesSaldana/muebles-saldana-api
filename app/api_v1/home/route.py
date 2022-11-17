from app.api_v1.api import api_router as router
from app.api_v1.home.schema import Images

@router.post('/home/images')
def create_images(images: Images):
    pass