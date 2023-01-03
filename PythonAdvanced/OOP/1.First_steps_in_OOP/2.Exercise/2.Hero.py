class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = int(health)

    def defend(self, damage):
        current_damage = int(damage)
        if current_damage >= self.health:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            self.health -= current_damage
            return None

    def heal(self, amount):
        amount = int(amount)
        self.health += amount
        return None
