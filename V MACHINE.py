# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:36:04 2025

@author: DELL
"""

def vending(drinks, snacks):
    print("VENDING MACHINE")
    print("Which category would you like?")
    print("Press")
    print("1 for drinks")
    print("2 for snacks")
    
    try:
        cat = int(input("Enter the category: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if cat == 1:
        handle_items(drinks, "drink")
    elif cat == 2:
        handle_items(snacks, "snack")
    else:
        print("Category not found, please try again")

def handle_items(items, item_type):
    print(f"Here is a list of {item_type}s:")
    for item in items:
        print(f"{item[0]} {item[1]} {item[2]} {item[3]} left")
    item_code = input("Enter the code for the item of your choice: ")
    
    for item in items:
        if item[0] == item_code:
            print("The price is:", item[2])
            try:
                paid = int(input("Please insert money: "))
            except ValueError:
                print("Invalid input. Please insert a valid amount.")
                return
            if paid >= item[2]:
                print("Thank you for purchasing")
                print("Here is your change:", paid - item[2])
                item[3] -= 1
                if item[3] == 0:
                    print(f"Sorry, {item_type} is out of stock")
            else:
                print("Insufficient funds, please try again.")
            return
    print(f"Invalid {item_type} code, please try again.")

def ask(drinks, snacks):
    userrans = input("Would you like to buy anything else? Press 'Y' for yes: ").strip().upper()
    if userrans == 'Y':
        vending(drinks, snacks)
    else:
        print("Thank you and goodbye!")

drinks = [['1', 'cola', 4, 12], ['2', 'juice', 5, 8], ['3', 'tea', 2, 21]]
snacks = [['1', 'chips', 5, 14], ['2', 'cookies', 4, 11], ['3', 'cake', 6, 4]]

vending(drinks, snacks)
ask(drinks, snacks)
