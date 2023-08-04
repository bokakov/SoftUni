# dough.py

class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        if not flour_type:
            raise ValueError("The flour type cannot be an empty string")
        if not baking_technique:
            raise ValueError("The baking technique cannot be an empty string")
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._flour_type = flour_type
        self._baking_technique = baking_technique
        self._weight = weight

    @property
    def flour_type(self):
        return self._flour_type

    @property
    def baking_technique(self):
        return self._baking_technique

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._weight = value
