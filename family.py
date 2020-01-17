from random import randint
class Family:
    def __init__(self, last_name):      #es lo que llamamos constructor
        self._last_name = last_name
        self._name = ""
        self._age = 0
        self._members = [{"id": 1, "name": "jorge", "lastname": "leyva", "age": 34}]

    def _generateId(self):
        return randint(0, 50)

    def add_member(self, member):
        member = {
            "id": self._generateId(),
            "name": member._name,
            "lastname": member._last_name,
            "age": member._age}
        self._members.append(member)
        return member

    def update_member(self, id, member):
        obj = self.get_member(id)
        obj.update(dict(member))
        return obj
      
    def delete_member(self, id):
        pass
        # obj = self.get_member(id)
        # obj.delete(dict(member))
        # return self._members

    def get_member(self, id): 
        member = list(filter(lambda item: item["id"] == id, self._members))
        return member[0]
        
    def get_all_members(self): 
        return self._members
