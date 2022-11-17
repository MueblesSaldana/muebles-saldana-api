class CategoryEntity:

    def get_entity(self, item):
        return {
            "id"    : str(item['_id']),
            "name"  : item['name']
        }

    def get_entitys(self, entity):
        return [self.get_entity(item) for item in entity]