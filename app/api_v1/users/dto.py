class Dto:

    def response(self, data):
        return {
            'message':  'Usuario creado con exito',
            'data':     data
        }


    def response_data(self, data):
        return {
            'message':  '',
            'data':     data
        }