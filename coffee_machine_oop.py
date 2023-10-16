# My code

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
#print(latte.name)
#print(latte.ingredients)
#print(espresso.cost)

menu = Menu()
menu.get_items()


coffee_maker = CoffeeMaker()

money_calculator = MoneyMachine() 

is_on = True

while is_on:
  order = input(f"What would you like? {menu.get_items()}: ")
  menu.find_drink(order)
  if order == "latte":
    coffee = latte
  elif order == "espresso":
    coffee = espresso
  elif  order == "cappuccino":
    coffee = cappuccino  

  
  if order == "off":
    id_on = False

  
  elif order == "report":
      print(coffee_maker.report())
      print(money_calculator.report())
  
  else:
      if coffee_maker.is_resource_sufficient(coffee):
          is_on = True
          if money_calculator.make_payment(coffee.cost):
              coffee_maker.make_coffee(coffee)



# teacher code

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
