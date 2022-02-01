#Coffe Machine
espresso_rate = 1.50
latte_rate = 2.50
cappuccino_rate = 3.00

report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

flavour_data = {

    "espresso": {
        "water": 50,
        "coffee": 18
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 150,
    },

}


def insert_coins():
    """Returns form the total calculated from the coins"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    amount_in_dollars = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return amount_in_dollars


def check_money(coins_inserted, flavour_rate, user_choice):
    """Calculate the refunding money and printing it"""
    if coins_inserted >= flavour_rate:
        refunded_money = coins_inserted - flavour_rate
        print("Here is ${:.2f} in change.".format(refunded_money))
        print(f"Here is your {user_choice} ☕️. Enjoy!")
        enough_money = True
        return enough_money

    else:
        print("Sorry that's not enough money. Money refunded.")
        enough_money = False
        return enough_money


def update_report(report, flavour_rate, flavour_data, user_choice):
    """Returns the updated resources"""
    updated_money_report = report["money"] + flavour_rate
    if user_choice == "espresso":
        updated_water_report = report["water"] - flavour_data[user_choice]["water"]
        updated_coffee_report = report["coffee"] - flavour_data[user_choice]["coffee"]
        return updated_water_report, updated_coffee_report, updated_money_report
    elif user_choice == "latte" or user_choice == "cappuccino":
        updated_milk_report = report["milk"] - flavour_data[user_choice]["milk"]
        updated_water_report = report["water"] - flavour_data[user_choice]["water"]
        updated_coffee_report = report["coffee"] - flavour_data[user_choice]["coffee"]
        return updated_water_report, updated_coffee_report, updated_milk_report, updated_money_report


def show_report(report):
    """Print the resources"""
    print(f"Water: {report['water']}ml\nMilk: {report['milk']}ml\nCoffee: {report['coffee']}g\nMoney: ${report['money']}")


coffee_machine_on = True
while coffee_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "espresso":
        if report["water"] >= 50 and report["coffee"] >= 18:
            coins_inserted = insert_coins()
            if check_money(coins_inserted, espresso_rate, user_choice):
                updated_water_report, updated_coffee_report, updated_money_report = update_report(report, espresso_rate,
                flavour_data, user_choice)
                report["water"] = updated_water_report
                report["coffee"] = updated_coffee_report
                report["money"] = updated_money_report

        elif report["water"] < 50:
            print("Sorry there is not enough water.")
        elif report["coffee"] < 18:
            print("Sorry there is not enough coffee.")

    elif user_choice == "latte":
        if report["water"] >= 200 and report["coffee"] >= 24 and report["milk"] >= 150:
            coins_inserted = insert_coins()
            if check_money(coins_inserted, latte_rate, user_choice):
                updated_water_report, updated_milk_report, updated_coffee_report, updated_money_report = update_report(report,
                latte_rate, flavour_data, user_choice)
                report["water"] = updated_water_report
                report["coffee"] = updated_coffee_report
                report["money"] = updated_money_report
                report["milk"] = updated_milk_report

        elif report["water"] < 200:
            print("Sorry there is not enough water.")
        elif report["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        elif report["milk"] < 150:
            print("Sorry there is not enough milk.")

    elif user_choice == "cappuccino":
        if report["water"] >= 250 and report["coffee"] >= 24 and report["milk"] >= 150:
            coins_inserted = insert_coins()
            if check_money(coins_inserted, cappuccino_rate, user_choice):
                updated_water_report, updated_milk_report, updated_coffee_report, updated_money_report = update_report(report,
                cappuccino_rate, flavour_data, user_choice)
                report["water"] = updated_water_report
                report["coffee"] = updated_coffee_report
                report["money"] = updated_money_report
                report["milk"] = updated_milk_report

        elif report["water"] < 250:
            print("Sorry there is not enough water.")
        elif report["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        elif report["milk"] < 150:
            print("Sorry there is not enough milk.")

    elif user_choice == "report":
        show_report(report)

    elif user_choice == "off":
        coffee_machine_on = False



# TODO: 1. User flavor choice
# TODO: 2. Stop the machine: off
# TODO: 3. Generate report: Water, Milk, Coffee, Money
# TODO: 4. Expresso: Money: $1.50, Water: 50ml, Coffee: 18g
# TODO: 4.1. Check if there are enough resources. If not: "Sorry there is not enough water."
# TODO: 4.2. Insert the coins. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01. If not enough money,
#  "Sorry that's not enough money. Money refunded.”. Else report updated. If too much money added then: “Here is $2.45
#  dollars in change." On successful deduction “Here is your latte. Enjoy!”.
# TODO: 5. Latte: Money: $2.50, Water: 200ml, Coffee: 24g, Milk: 150ml
# TODO: 5.1. Check if there are enough resources. If not: "Sorry there is not enough water."
# TODO: 5.2. Insert the coins. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01. If not enough money,
#  "Sorry that's not enough money. Money refunded.”. Else report updated. If too much money added then: “Here is $2.45
#  dollars in change." On successful deduction “Here is your latte. Enjoy!”.
# TODO: 6. Cappuccino: Money: $3.00, Water: 250ml, Coffee: 24g, Milk: 150ml
# TODO: 6.1. Check if there are enough resources. If not: "Sorry there is not enough water."
# TODO: 6.2. Insert the coins. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01. If not enough money,
#  "Sorry that's not enough money. Money refunded.”. Else report updated. If too much money added then: “Here is $2.45
#  dollars in change." On successful deduction “Here is your latte. Enjoy!”.
