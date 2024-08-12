
class Items:

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    # TODO: Getter and Setters for accessing the name, price, description


class UIInterface:

    def __init__(self, items):
        self.items = items

    # TODO: Add permission for Admin
    def add_item(self, item):
        self.items.append(item)

    # TODO: Add permission for Admin
    def remove_item(self, item):
        self.items.remove(item)

    def get_all_items(self):
        return self.format(self.items)

    def get_filtered_items(self, term):
        filter_items = [
            item for item in self.items if item.name.startswith(term)
        ]
        return self.format(filter_items)

    def format(self, items):
        return [
            {'name': item.name, 'price': item.price} for item in items
        ]

