class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {','.join(Pet.PET_TYPES)}") 
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet should be an instance of the pet class.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name) 
        