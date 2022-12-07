def mainMenu():
    while True:
        print()
        print('''SHOPPING LIST

        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        ''')


        selection = input("Make your selection: ")


        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        else:
            print("You did not make a valid selection.")


shopping_list = ["milk", "eggs", "flour", "rice","oranges","apples"]


def displayList():
    print()
    print("---SHOPPING LIST---")
    for i in shopping_list:
        print("* " + i)

def addItem():
    item = input("Enter item you wish to add to the shopping list: ")
    shopping_list.append(item)
    print(item + " has been added to the shopping list.")

def removeItem():
    item = input("Which item would you like to remove from the shopping list: ")
    shopping_list.remove(item)
    print(item + " has been removed from the shopping list.")

def checkItem():
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes, " + item + " is on the shopping list.")
    else:
        print("No, " + item + " is not on the shopping list.")

def listLength():
    print("There are", len(shopping_list), "items on the shopping list.")

def clearList():
    shopping_list.clear()
    print("The shopping list is now empty.")

mainMenu()