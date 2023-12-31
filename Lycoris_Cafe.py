# Team Name: Lycoris Cafe
# Members: Dasun Nethsara
#          Naveen Balasooriya
#          Lasith Randil

# imports
import platform
import ast
import os

# solution for colorama init function error in different python versions
try:
    from colorama import Fore, init

    init(convert=True)
except NameError:
    from colorama import Fore

# external functions
from functions import *

# important variables or constants
cpu_number: dict = {}
ram_number: dict = {}
hdd_number: dict = {}
mb_number: dict = {}
psu_number: dict = {}
case_number: dict = {}
scren_number: dict = {}
currently_loggedIn: str = ""


# top header
def decorations():
    """This is a TOP Header"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")
    print(
        Fore.CYAN
        + """
            ================================
            =  Welcome to Lycoris PC Mart  =
            ================================
          """
    )
    if not currently_loggedIn == "":
        print("\n" + Fore.YELLOW + f"Hello {currently_loggedIn}!")


def home(
    cpu_number: dict,
    ram_number: dict,
    hdd_number: dict,
    mb_number: dict,
    psu_number: dict,
    case_number: dict,
    scren_number: dict,
):
    global currently_loggedIn
    while True:
        decorations()
        print(
            Fore.GREEN
            + """
[1] - PC Accessories
[2] - Cart
[3] - Exit
"""
        )
        try:
            userChoice: int = int(input(f">>> {Fore.YELLOW}"))
            if userChoice == 1:
                pcAccessories(
                    cpu_number,
                    ram_number,
                    hdd_number,
                    mb_number,
                    psu_number,
                    case_number,
                    scren_number,
                )
            elif userChoice == 2:
                showShoppingCart(currently_loggedIn)
            elif userChoice == 3:
                currently_loggedIn = ""
                decorations()
                print("Bye!")
                exit(1)
        except ValueError:
            continue


def pcAccessories(
    cpu_number: dict,
    ram_number: dict,
    hdd_number: dict,
    mb_number: dict,
    psu_number: dict,
    case_number: dict,
    scren_number: dict,
):
    global currently_loggedIn
    while True:
        decorations()
        print(
            Fore.GREEN
            + """
We have,
  [1] - CPU
  [2] - RAM
  [3] - HDD/SSD
  [4] - Motherboard
  [5] - Power Supply Unit
  [6] - Casing
  [7] - Monitor
  [99] - Go Back
                """
        )

        user: int = int(input(">>> " + Fore.YELLOW))

        if user == 1:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                cpuList(cpu_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(cpu_number):
                    decorations()
                    items = getCpuData(choice, cpu_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 2:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                ramList(ram_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(ram_number):
                    decorations()
                    items = getRamData(choice, ram_number)
                    print(Fore.GREEN + "\n[1] - Add to cart \n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 3:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                hddList(hdd_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(hdd_number):
                    decorations()
                    items = getHddData(choice, hdd_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 4:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                mbList(mb_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(mb_number):
                    decorations()
                    items = getMbData(choice, mb_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 5:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                psuList(psu_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(psu_number):
                    decorations()
                    items = getPsuData(choice, psu_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 6:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                casingList(case_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(case_number):
                    decorations()
                    items = getCasingData(choice, case_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 7:
            while True:
                decorations()
                print(Fore.GREEN + "\nWe have,")
                scrnList(scren_number)
                print("\n(For more info., input item number)\n[99] - Back\n")
                choice: int = int(input(">>> " + Fore.YELLOW))
                if choice <= len(scren_number):
                    decorations()
                    items = getScrnData(choice, scren_number)
                    print(Fore.GREEN + "\n[1] - Add to cart\n[2] - Back\n")
                    choice2: int = int(input(">>> " + Fore.YELLOW))
                    if choice2 == 2:
                        break
                    elif choice2 == 1:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 99:
            home(
                cpu_number,
                ram_number,
                hdd_number,
                mb_number,
                psu_number,
                case_number,
                scren_number,
            )


def showShoppingCart(currently_loggedIn: str):
    decorations()
    print(Fore.GREEN + "\nYour Cart")
    filename = f"./cart/{currently_loggedIn}.txt"
    file = open(filename, "r")
    cartItems = file.readlines()
    # cartItems = cartItems.replace("\n", "")
    # Process each line to extract item name and price
    cart = []
    for line in cartItems:
        item_dict = ast.literal_eval(line)
        cart.append(item_dict)

    total: float = 0
    count: int = 1
    # Display the cart items line by line
    for item in cart:
        item_name = list(item.keys())[0]
        item_price = item[item_name]
        print(f"\t{count}. {item_name}: {item_price}USD")
        total += float(item_price)
        count += 1
    print("\n")
    print(f"Total Items: {Fore.YELLOW}{count}")
    print(f"{Fore.GREEN}Total Payments: {Fore.YELLOW}{round(total, 2)}USD")

    # Allow the user to remove items
    print(Fore.GREEN + "\n[1] - Get a Excel Sheet\n[2] - Remove an Item\n[99] - Back\n")
    choice: str = input(">>> " + Fore.YELLOW)

    if choice == "1":
        writeToExcel(currently_loggedIn)

    elif choice == "2":
        remove_item = input("Enter the item name to remove: ")
        found = False
        for item in cart:
            if remove_item in item:
                cart.remove(item)
                found = True
                print(f"{Fore.YELLOW}{remove_item} removed from the cart.")
                break
            if not found:
                print(Fore.RED + "Item not found in the cart.")

    elif choice == 99:
        pass
    else:
        pass

    # Write the updated cart data back to the file
    with open(filename, "w") as file:
        for item in cart:
            file.write(str(item) + "\n")


if __name__ == "__main__":
    if currently_loggedIn == "":
        decorations()
        u = login()
        currently_loggedIn = u
        home(
            cpu_number,
            ram_number,
            hdd_number,
            mb_number,
            psu_number,
            case_number,
            scren_number,
        )
