
from abc import ABC, abstractmethod


class PaymentTypes(ABC):

    @abstractmethod
    def complete_payment(self, amount):
        pass

class CardPayment(PaymentTypes):

    # def __init__(self, expiry, cvv, card_no, owner_name):
        # TODO: handle payment

    def complete_payment(self, amount):
        print(f"Payment Processing by Card for {amount}")
        print("Payment Completed by Card ...")


class UPIPayment(PaymentTypes):

    # def __init__(self, upi_id, pin):
        # Handling payment initialization

    def complete_payment(self, amount):
        print(f"Payment Processing by UPI for {amount}")
        print("Payment Completed by UPI")


class PaymentProcess:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def complete_payment(self, amount):
        self.payment_method.complete_payment(amount)

