
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

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["lastname"] = self.last_name
        if "id" not in member : 
            member["id"] = self._generateId()
        self._members.append(member)
        return member
        pass

    def delete_member(self, id):
        # fill this method and update the return
        if any(d['id'] == id for d in self._members):
            self._members = list(filter(lambda i: i["id"] != id,self._members))
            return {"msg" : "member removed"}
        return {"result" : "member not found"}
        pass

    def get_member(self, id):
        # fill this method and update the return
        if any(d['id'] == id for d in self._members):
            self._members = list(filter(lambda i: i["id"] != id,self._members))
            return {"msg" : "member removed"}
        return {"result" : "member not found"}
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
