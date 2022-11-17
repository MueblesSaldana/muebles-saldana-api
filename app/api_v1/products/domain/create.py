from app.api_v1.products.schemas.create import CreateProduct
from app.api_v1.products.dao import Dao
from app.api_v1.products.model import ProductsEntity
from fastapi.responses import JSONResponse
from app.core.handlers import convert_base_img, convert_bytes
import sys, cloudinary.uploader


class Create:
    def execute(self, product: CreateProduct):
        try:
            __prod = Dao().get_one_by_name(product.name)
            if __prod:
                return JSONResponse(content='El producto ya existe', status_code=400)
           
            __imgs = []
            ##Process imgs
            for imgs in product.images:
                image           = convert_base_img(imgs['base'])
                img_size_bytes  = sys.getsizeof(image)
                img_size_mb     = convert_bytes(img_size_bytes,'m')

                url = cloudinary.uploader.upload(image, folder='products/imgs')
                print(url)
                __imgs.append(
                    {
                        'url': url['secure_url'], 
                        'id': url['public_id']
                    }
                )

            product.images = __imgs
            print(__imgs[0:2])
            product.images_item = __imgs[0:2]

            product = Dao().create(product)

            if type(product) is JSONResponse:
                return product

            response = ProductsEntity().get_entity(product)

            return {
                'message': 'Producto creado con exito',
                'data':     response
            }

        except Exception as err:
            print('Create: ', err)