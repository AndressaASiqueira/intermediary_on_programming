# My code

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#coffee_emoji = "☕"

water = (resources["water"])
milk = (resources["milk"])
coffee = resources["coffee"]
money = 0
    #print(water, milk, coffee, money)

water_espresso = (MENU["espresso"]["ingredients"]["water"])
coffee_expresso = (MENU["espresso"]["ingredients"]["coffee"])
cost_espresso = (MENU["espresso"]["cost"])
    #print(water_espresso, coffee_expresso, cost_espresso)

water_latte = (MENU["latte"]["ingredients"]["water"])
milk_latte = (MENU["latte"]["ingredients"]["milk"])
coffee_latte = (MENU["latte"]["ingredients"]["coffee"])
cost_latte = (MENU["latte"]["cost"])
    #print(water_latte, milk_latte, coffee_latte, cost_latte)

water_cappuccino = (MENU["cappuccino"]["ingredients"]["water"])
milk_cappuccino = (MENU["cappuccino"]["ingredients"]["milk"])
coffee_cappuccino = (MENU["cappuccino"]["ingredients"]["coffee"])
cost_cappuccino = (MENU["cappuccino"]["cost"])
    #print(water_cappuccino, milk_cappuccino, coffee_cappuccino, coffee_cappuccino)

end = True
def coins(order):
        """Input the type of coffee and amount of money to return if the it has enough money, the chargue and how many has in resources"""
        print("Please insert coins.")
        quarters = float(input("how many quarters?: ")) * 0.25
        dimes = float(input("how many dimes?: ")) * 0.10
        nickles = float(input("how many nickles?: ")) * 0.05
        pennies = float(input("how many pennies?: ")) * 0.01
        #print(quarters)

        amount = quarters + dimes + nickles + pennies
        amount = (round(amount, 2))

        if order == "espresso":
            amount -= 1.5
        elif order == "latte":
            amount -= 2.5
        elif order == "cappuccino":
            amount -= 3.0
        
        return amount

#def coffee_machine():
while end:
    order = input("What would you like? (espresso/latte/cappuccino): ")
        #coffee_machine()
    # ask which type of coffee
    # create a function to calculate the amount of resources when an order is made.
    resources_left = 10
    if order == "off":
        end = False
        resources_left = 0 

    if order == "espresso":
      if water >=water_espresso:
       water -=water_espresso
       
      else:
            print("Sorry, not enough water")
            resources_left = 0
      if coffee >= coffee_expresso:
            coffee -=coffee_expresso
      else: 
            print("Sorry, not enough coffee") 


    elif order == "latte":
        if water >=water_latte:
            water -=water_latte
        else:
            print(water)
            print("Sorry, not enough water")
            resources_left = 0
            
        if milk >= milk_latte:
            milk -=milk_latte
            print(milk)
        else:
            print("Sorry, not enough milk")
            
        if coffee >= coffee_latte:
            coffee -=coffee_latte
            #print(coffee)
        else: 
            print("Sorry, not enough coffee")
            

    elif order == "cappuccino":
        if water >=water_cappuccino:
            water-=water_cappuccino
        else:
            print("Sorry, not enough water")
            resources_left = 0 
            
        if milk >= milk_cappuccino:
            milk -=milk_cappuccino
            print(milk)
        else:
            print("Sorry, not enough milk")
            
        if coffee >= coffee_cappuccino:
            coffee -=coffee_cappuccino
            #print(coffee)
        else: 
            print("Sorry, not enough coffee")
        #coffee_machine()

    elif order == "resources":
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: {money}")

    if resources_left != 0 and order != "resources": 
        amount = coins(order)
        #print(amount)
        if amount > 0:
           print(f"Here is ${amount} in change.")
           print(f"Here is your {order} ☕️. Enjoy!") 
           if order == "espresso":
               money += 1.5
           elif order == "latte":
              money += 2.5 
           elif order == "cappuccino":
                money += 3.0  
        elif amount < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is your {order} ☕️. Enjoy!") 

    # if any resources are insufficient tell it and ask again for a new coffee
    # if it has enough resources ask for the money

#print("Here is $10.0 in change.")
#print("Here is your latte ☕️. Enjoy!")


# if the money is enough say it, return what is left and store the coffee value in the resources
# create a function to calculate the money 
# if the money is not enough say it and ask another coffee
# put the value of the made coffee in the variable money
# if the coffee is made say enjoy and ask another
# if type off the program will stop
# if type report show how many resources including the money


#Teacher code

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
