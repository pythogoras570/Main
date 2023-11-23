from project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = dict(toppings)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        value = self.__name

    @property
    def dough(self):
        return

    @dough.setter
    def dough(self, value):
        pass

    @property
    def max_number_of_toppings(self):
        return self.max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError('The maximum number of toppings cannot be less or equal to zero')
        value = self.max_number_of_toppings

    @property
    def toppings(self):
        return

    @toppings.setter
    def toppings(self, value):
        pass