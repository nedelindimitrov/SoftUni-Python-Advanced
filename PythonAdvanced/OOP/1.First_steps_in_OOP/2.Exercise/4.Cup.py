class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, amount):
        current_amount = int(amount)
        free_space = self.size - self.quantity
        if current_amount > free_space:
            return None
        self.quantity += current_amount

    def status(self):
        free_space = self.size - self.quantity
        return free_space
