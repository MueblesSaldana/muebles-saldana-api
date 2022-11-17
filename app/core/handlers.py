import base64

def convert_bytes(bytes, to, bsize=1024): 
    try:
        a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
        r = float(bytes)
        return (r / (bsize ** a[to]))
    except Exception as err:
        print('core', 'handle', 'convert_base_img', err, 'ERROR_CONVERT_BYTES')

#Funcion para decodificar imagen
def convert_base_img(base: str):
    
    try:
        image_64_decode = base64.b64decode(base)
        return image_64_decode
    except Exception as err:
       print('core', 'handle', 'convert_base_img', err, 'ERROR_CONVERT_BASE_IMG')