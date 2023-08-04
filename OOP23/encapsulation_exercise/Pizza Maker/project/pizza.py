# pizza.py

class Pizza:
    def __init__(self, name, dough, max_number_of_toppings):
        if not name:
            raise ValueError("The name cannot be an empty string")
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        if max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    def add_topping(self, topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings.values())
        return total_weight
