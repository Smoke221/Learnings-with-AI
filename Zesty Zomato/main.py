import json
from tabulate import tabulate

menu = {}

# Function to save the menu to a file
def save_menu_to_file():
    with open('menu.json', 'w') as file:
        json.dump(menu, file)

# Function to load the menu from menu.json
def load_menu_from_file():
    with open('menu.json', 'r') as file:
        menu_data = json.load(file)
    return menu_data

# Function add a dish to the menu
def add_menu():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    dish_price = input("Enter dish price: ")
    dish_availability = input("Is the dish available? (yes/no): ")

    menu[dish_id] = {
        "dish_name": dish_name,
        "dish_price": dish_price,
        "dish_availability": dish_availability.lower() == "yes"
    }
    save_menu_to_file()  # Save the updated menu data
    print("Dish added to the menu successfully")

# Function to remove a dish from the menu
def remove_dish():
    dish_ID = input("Enter Dish ID you wish to remove from the menu: ")
    menu_data = load_menu_from_file()
    if dish_ID in menu_data:
        del menu_data[dish_ID]
        menu.clear()
        menu.update(menu_data)
        save_menu_to_file()  # Update the menu file
        print(f"The dish has been removed from the menu.")
    else:
        print(f"The dish is not found in the menu.")


# Function to display menu
def display_menu(menu_data):
    table = []
    for dish, details in menu_data.items():
        row = [dish, details["dish_name"], details["dish_price"], details["dish_availability"]]
        table.append(row)
    headers = ["Dish ID","Name","Price","Availability"]
    print(tabulate(table, headers, tablefmt="grid"))

# user's input
while True:
    print("\n*** Welcome to zesty zomato ***")
    print("1. Add a dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update the availability of a dish")
    print("4. Display menu")
    print("5. Take an order from a customer")
    print("6. Update the status of the order")
    print("7. View all the orders")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_menu()
    elif choice == "2":
        remove_dish()
    elif choice == "3":
        update_dish()
    elif choice == "4":
        menu_data = load_menu_from_file()
        display_menu(menu_data)
    elif choice == "5":
        take_order()
    elif choice == "6":
        order_status()
    elif choice == "7":
        all_orders()
    elif choice == "0":
        print("Thank you for exploring Zesty Zomato. See you soon...")
        break
    else:
        print("Invalid choice. Please try again") 
