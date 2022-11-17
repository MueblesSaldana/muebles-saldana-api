class SubCategoryEntity:

    def get_entity(self, item):
        return {
            "id"            : str(item['_id']),
            "name"          : item['name'],
            "category_id"   : item['category_id'],
            "category_name" : item['category_name']
        }

    def get_entitys(self, entity):
        return [self.get_entity(item) for item in entity]