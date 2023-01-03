class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def water(self, quantity):
        current_amount = int(quantity)
        if current_amount >= self.water_requirements:
            self.is_happy = True
        if current_amount < self.water_requirements:
            self.is_happy = False

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"
