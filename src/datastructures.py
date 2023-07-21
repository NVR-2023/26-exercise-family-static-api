from random import randint


# Data Initialziation

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3] 
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Methods: Add family member

    def add_member(self, member):
        if type(member['first_name']) is not str: return False 
        if type(member['age']) is not int: return False
        if type(member['lucky_numbers']) is not list: return False
        
        if member.get('id') is None:
            member['id'] = self._generate_id()
        
        member['last_name'] = self.last_name
        self._members.append(member)
        return True

    # Methods: Delete family member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}
        return {"done": False}

    # Methods: GET speciifc  family member

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return False
    

    # Methods: GET all family members, serialized

    def get_all_members(self):
        return [
            {
                "id": member['id'],
                "first_name": member['first_name'],
                "last_name": self.last_name,
                "age": member['age'],
                "lucky_numbers": member['lucky_numbers']
            }
            for member in self._members
        ]

    def _generate_id(self):
        return randint(0, 99)