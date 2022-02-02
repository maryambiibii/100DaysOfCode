from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Objects created for classes
menu_class = Menu()
coffee_maker_class = CoffeeMaker()
money_machine_class = MoneyMachine()

machine_status = True
while machine_status:
    choice = menu_class.get_items()
    order_name = input(f"What would you like? {choice} ").lower()
    if order_name == "off":
        machine_status = False
    elif order_name == "report":
        coffee_maker_class.report()
        money_machine_class.report()
    else:
        drink_ordered = menu_class.find_drink(order_name)
        if coffee_maker_class.is_resource_sufficient(drink_ordered):
            if money_machine_class.make_payment(drink_ordered.cost):
                coffee_maker_class.make_coffee(drink_ordered)

