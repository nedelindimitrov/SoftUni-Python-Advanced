class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.items_count = 0

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.items_count == self.capacity:
            return f"Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.items_count += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"
        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items_count -= amount
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
