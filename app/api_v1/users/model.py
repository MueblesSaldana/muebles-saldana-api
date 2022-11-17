class UsersEntity:
    def user_entity(self, item):
        return {
            'id':         str(item['_id']),
            'name':       item['name'],
            'lastname':   item['lastname'],
            'user_name':  item['user_name'],
            'email':      item['email'],
            'password':   item['password']
        }

    def users_entity(self, entity):
        return [self.user_entity(item) for item in entity]
