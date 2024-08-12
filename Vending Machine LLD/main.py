
from VendingMachineManager import VendingMachineManager
from UIInterface import UIInterface, Items
from PaymentProcess import CardPayment



# Client side code
# Can be moved to  a common facade
item1 = Items('Pasta', 60, 'Pasta')
item2 = Items('Dal', 70, 'Dal')
item3 = Items('Shampoo', 80, 'Shampoo')
item4 = Items('Sattu', 45, '')
item5 = Items('Thumps up', 40, '')
item6 = Items('Lays', 20, '')
item7 = Items('Pass Pass', 10, '')
ui_interface = UIInterface([item1, item2, item3, item4, item5, item6])
ui_interface.add_item(item7)
ui_interface.remove_item(item5)
print([item.name for item in ui_interface.items])

vending_manager = VendingMachineManager(ui_interface)

print(vending_manager.show_items())
print(vending_manager.show_filtered_items('Pa'))

vending_manager.start_processing()
vending_manager.add_item(item1)
vending_manager.add_item(item1)
vending_manager.add_item(item1)
vending_manager.add_item(item1)
vending_manager.remove_item(item1)
vending_manager.add_item(item3)
vending_manager.add_item(item6)
print(vending_manager.get_amount())
vending_manager.add_item(item3)
print(vending_manager.complete_processing())

vending_manager.start_payment(CardPayment())
vending_manager.complete_payment()

