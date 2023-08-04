import unittest

class Vet:
    # Class attributes
    animals_total = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(self.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals_total.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals_total.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        number_animals = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals_total)
        return f"{self.name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


class Tests(unittest.TestCase):
    def test_init(self):
        vet = Vet("Bob")
        Vet.animals_total = []
        Vet.space = 5
        self.assertEqual(vet.name, "Bob")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals_total, [])
        self.assertEqual(Vet.space, 5)

    def test_register_successfull(self):
        vet = Vet("Bob")
        Vet.animals_total = []
        Vet.space = 5
        vet2 = Vet("Peter")
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Doggy registered in the clinic")
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet2.animals, [])

    def test_register_unsuccessfull(self):
        vet = Vet("Bob")
        Vet.animals_total = []
        Vet.space = 5
        for i in range(6):
            vet.register_animal(str(i))
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Not enough space")
        self.assertEqual(len(Vet.animals_total), 5)
        self.assertEqual(len(vet.animals), 5)

    def test_unregister_successfull(self):
        vet = Vet("Bob")
        Vet.animals_total = []
        Vet.space = 5
        vet.register_animal("Kitty")
        res = vet.unregister_animal("Kitty")
        self.assertEqual(res, "Kitty unregistered successfully")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals_total, [])


if __name__ == "__main__":
    unittest.main()
\