

class CartHandler:

    def __init__(self):
        self.selected_items = []    # {'item': item, 'quantity': quantity}
        self.total_cost = 0

    def show_selected_items(self):
        return [
            {'item': item['item'].name, 'quantity': item['quantity']} for item in self.selected_items
        ]

    def add_item(self, new_item):
        self.total_cost += new_item.price
        for item in self.selected_items:
            if item['item'] == new_item:
                item['quantity'] += 1
                return
        self.selected_items.append({
            'item': new_item,
            'quantity': 1
        })

    def remove_item(self, new_item):
        for item in self.selected_items:
            if item['item'] == new_item:
                item['quantity'] -= 1
                if item['quantity'] == 0:
                    self.selected_items.remove(item)
                self.total_cost -= new_item.price
                return
        raise ValueError(f"No item of this type present")

    def get_total_cost(self):
        return self.total_cost

