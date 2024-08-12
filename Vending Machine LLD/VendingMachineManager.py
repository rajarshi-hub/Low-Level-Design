from PaymentProcess import PaymentProcess
from CartHandler import CartHandler


class VendingMachineManager:

    def __init__(self, ui_interface):
        self.ui_interface = ui_interface
        self.cart_manager = None
        self.payment = None

    def show_items(self):
        return self.ui_interface.get_all_items()

    def start_processing(self):
        self.cart_manager = CartHandler()

    def complete_processing(self):
        return self.cart_manager.get_total_cost(), self.cart_manager.show_selected_items()

    def show_filtered_items(self, term):
        return self.ui_interface.get_filtered_items(term)

    def add_item(self, item):
        self.cart_manager.add_item(item)

    def remove_item(self, item):
        self.cart_manager.remove_item(item)

    def get_amount(self):
        return self.cart_manager.get_total_cost()

    def start_payment(self, payment_method):
        self.payment = PaymentProcess(payment_method)

    def complete_payment(self):
        self.payment.complete_payment(self.get_amount())


