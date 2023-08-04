class Player:
    def __init__(self, name: str, age: int, stamina: int = 100):
        if name == '':
            raise ValueError("Name not valid!")
        self.name = name
        self.age = age
        if age < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.stamina = stamina
        if stamina < 0 or stamina > 100:
            raise ValueError("Stamina not valid!")

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
