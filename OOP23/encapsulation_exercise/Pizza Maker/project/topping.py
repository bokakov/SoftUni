# topping.py

class Topping:
    def __init__(self, topping_type, weight):
        if not topping_type:
            raise ValueError("The topping type cannot be an empty string")
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._topping_type = topping_type
        self._weight = weight

    @property
    def topping_type(self):
        return self._topping_type

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._weight = value
