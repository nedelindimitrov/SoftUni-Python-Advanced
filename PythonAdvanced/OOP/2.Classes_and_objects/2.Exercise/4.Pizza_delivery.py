class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.pizza_ordered()
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            price_to_add = quantity * price_per_quantity
            self.price += price_to_add
            return None
        self.ingredients[ingredient] += quantity
        price_to_add = quantity * price_per_quantity
        self.price += price_to_add

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.pizza_ordered()
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        price_to_decrease = quantity * price_per_quantity
        self.price -= price_to_decrease

    def make_order(self):
        if self.ordered:
            return self.pizza_ordered()
        self.ordered = True
        string_to_use = ', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {string_to_use} and the price will be {self.price}lv."

    def pizza_ordered(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"
