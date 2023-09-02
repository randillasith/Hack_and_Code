# imports
import ast

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
        userChoice: int = int(
            input(
                "\n[1] - PC Accessories\n[2] - Cart\n[3] - Exit\n What do you want? >>> "
            )
        )
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
            exit(1)


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
        print(
            """We have,
            1 - CPU
            2 - RAM
            3 - HDD/SSD
            4 - Motherboard
            5 - Power Supply Unit
            6 - Casing
            7 - Monitor
            8 - Go Back"""
        )

        user: int = int(input("What do you want? >>> "))

        if user == 1:
            while True:
                print("We have, \n")
                cpuList(cpu_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(cpu_number):
                    items = getCpuData(choice, cpu_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 2:
            while True:
                print("We have, \n")
                ramList(ram_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(ram_number):
                    items = getRamData(choice, ram_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 3:
            while True:
                print("We have, \n")
                hddList(hdd_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(hdd_number):
                    items = getHddData(choice, hdd_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 4:
            while True:
                print("We have, \n")
                mbList(mb_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(mb_number):
                    items = getMbData(choice, mb_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 5:
            while True:
                print("We have, \n")
                psuList(psu_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(psu_number):
                    items = getPsuData(choice, psu_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 6:
            while True:
                print("We have, \n")
                casingList(case_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(case_number):
                    items = getCasingData(choice, case_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 7:
            while True:
                print("We have, \n")
                scrnList(scren_number)
                print("\n [n] - More Details\n [99] - Back")
                choice: int = int(input(">>> "))
                if choice <= len(scren_number):
                    items = getScrnData(choice, scren_number)
                    choice2: int = int(
                        input("\n [1] - Back \n [2] - Add to cart\n>>> ")
                    )
                    if choice2 == 1:
                        break
                    elif choice2 == 2:
                        addItemsToCart(items[0], items[1], currently_loggedIn)
                    else:
                        pass
                elif choice == 99:
                    break
        elif user == 8:
            if currently_loggedIn == "":
                home(
                    cpu_number,
                    ram_number,
                    hdd_number,
                    mb_number,
                    psu_number,
                    case_number,
                    scren_number,
                )
            else:
                exit(1)


# for i in cartItems:
#         res.append(i.replace("\n", ""))
def showShoppingCart(currently_loggedIn: str):
    print("\n Your Cart")
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
    count: int = 0
    # Display the cart items line by line
    for item in cart:
        item_name = list(item.keys())[0]
        item_price = item[item_name]
        print(f"\t{item_name}: {item_price}USD")
        total += float(item_price)
        count += 1
    print("\n")
    print(f"Total Items: {count}")
    print(f"Total Payments: {total}")

    # Allow the user to remove items
    remove_item = input("Enter the item name to remove ('q' to quit): ")
    found = False
    if remove_item != "q":
        for item in cart:
            if remove_item in item:
                cart.remove(item)
                found = True
                print(f"{remove_item} removed from the cart.")
                break
        if not found:
            print("Item not found in the cart.")
    else:
        pass

    # Write the updated cart data back to the file
    with open(filename, "w") as file:
        for item in cart:
            file.write(str(item) + "\n")


print("\n Welcome to Lycoris PC Mart")


if __name__ == "__main__":
    if currently_loggedIn == "":
        u = login()
        currently_loggedIn = u
        print(f"Hello {currently_loggedIn}!")
        home(
            cpu_number,
            ram_number,
            hdd_number,
            mb_number,
            psu_number,
            case_number,
            scren_number,
        )
