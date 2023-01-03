class Shop():
    def __init__(self, name, items):
        self.name = name
        self.items = list(items)

    def get_items_count(self):
        current_list = self.items
        current_len = len(current_list)
        return current_len
