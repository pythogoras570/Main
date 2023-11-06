from typing import Dict


class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: Dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        pass

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        pass

    def make_order(self):
        pass