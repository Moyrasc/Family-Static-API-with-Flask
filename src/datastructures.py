
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        
        self._members.append(member)
        return self._members
        pass

    def delete_member(self, id):
       
        self._members = list(filter(lambda item: id!=item["id"], self._members))
        return None
        pass

    def get_member(self, id):
      
        for member in self._members:
            if id==member["id"]:
                return member
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
