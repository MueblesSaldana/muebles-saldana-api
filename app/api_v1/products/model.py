class ProductsEntity:

    def get_entity(self, item):
        return {
            "id"                    : str(item['_id']),
            'name'                  : item['name'],
            'description'           : item['description'],
            'category_id'           : item['category_id'],
            'category_name'         : item['category_name'],
            'sub_category_id'       : item['sub_category_id'],
            'sub_category_name'     : item['sub_category_name'],
            'price'                 : item['price'],
            'old_price'             : item['old_price'],
            'quantity'              : item['quantity'],
            'images'                : item['images'],
            'images_item'           : item['images_item']
        }

    def get_entitys(self, entity):
        return [self.get_entity(item) for item in entity]