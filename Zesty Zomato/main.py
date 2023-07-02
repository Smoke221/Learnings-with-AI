import json
from tabulate import tabulate

menu = {}
orders = {}
order_ID = 1

# Function to save the menu to a file
def save_menu_to_file():
    with open('menu.json', 'w') as file:
        json.dump(menu, file)

# Function to load the menu from menu.json
def load_menu_from_file():
    with open('menu.json', 'r') as file:
        menu_data = json.load(file)
    return menu_data

# Function to save the orders to a file
def save_orders_to_file():
    with open('orders.json', 'w') as file:
        json.dump(orders, file)

# Function to load the orders from orders.json
def load_orders_from_file():
    with open('orders.json', 'r') as file:
        orders_data = json.load(file)
    return orders_data

# Function add a dish to the menu
def add_menu():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    dish_price = input("Enter dish price: ")
    dish_availability = input("Is the dish available? (yes/no): ")

    if dish_availability == "yes":
        stock = input("Available stock: ")
    else:
        stock = "N/A"

    menu[dish_id] = {
        "dish_name": dish_name,
        "dish_price": dish_price,
        "dish_availability": dish_availability.lower() == "yes",
        "stock": stock
    }
    save_menu_to_file()  # Save the updated menu data
    print("Dish added to the menu successfully")

# Function to remove a dish from the menu
def remove_dish():
    dish_ID = input("Enter the dish ID you wish to remove from the menu: ")
    menu_data = load_menu_from_file()
    if dish_ID in menu_data:
        del menu_data[dish_ID]
        menu.clear()
        menu.update(menu_data)
        save_menu_to_file()  # Update the menu file
        print(f"The dish has been removed from the menu.")
    else:
        print(f"The dish is not found in the menu.")

# Function to update the availability of the dish
def update_dish():
    dish_ID = input("Enter the dish ID to update availability: ")
    menu_data = load_menu_from_file()
    if dish_ID in menu_data:
        new_availability = input("Is the dish available? (yes/no): ").lower()
        menu_data[dish_ID]["dish_availability"] = new_availability == "yes"
        if new_availability == "yes":
            stock = input("Available stock: ")
            menu_data[dish_ID]["stock"] = stock
        else:
            menu_data[dish_ID]["stock"] = "N/A"

        save_menu_to_file()
        menu.clear()
        menu.update(menu_data) 
        print("Dish availability updated successfully.")
    else:
        print("The dish is not found in the menu.")
# Function to display menu
def display_menu(menu_data):
    table = []
    for dish, details in menu_data.items():
        row = [dish, details["dish_name"], details["dish_price"], details["dish_availability"]]
        table.append(row)
    headers = ["Dish ID","Name","Price","Availability"]
    table_formatted = tabulate(table, headers, tablefmt="grid")
    colored_table = "\033[36m" + table_formatted + "\033[0m"  # Cyan color
    print(colored_table)

# Function to take an order from a customer
def take_order():
    global order_ID
    customer_name = input("Enter the customer's name: ")
    dish_IDs = input("Enter the dish IDs (sperated by comma): ").split(",")

    order_dishes = []
    order_status = "received"

    for dish_ID in dish_IDs:
        if dish_ID in menu and menu[dish_ID]["dish_availability"]:
            order_dishes.append(menu[dish_ID]["dish_name"])
        else:
            print(f"Dish with ID {dish_ID} is not available")

    if order_dishes:
        order_id = str(order_ID)
        orders[order_id] = {
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": order_status
        }
        order_ID += 1
        save_orders_to_file()
        print("Order placed successfully.")
    else:
        print("No dishes available to place the order.")

#Function to update the status of an order
def update_order_status():
    order_id = input("Enter the order ID: ")
    if order_id in orders:
        new_status = input("Enter the new status: ")
        orders[order_id]["status"] = new_status
        save_orders_to_file()
        print("Order status updated successfully")
    else:
        print("Invalid order ID.")

# Function to view all the orders
def all_orders():
    table = []
    for order_id, order_details in orders.items():
        row = [order_id, order_details["customer_name"], ", ".join(order_details["dishes"]), order_details["status"]]
        table.append(row)
    headers = ["Order ID", "Customer Name", "Dishes", "Status"]
    table_formatted = tabulate(table, headers, tablefmt="grid")
    colored_table = "\033[35m" + table_formatted + "\033[0m"  # Magenta color
    print(colored_table)

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
        update_order_status()
    elif choice == "7":
        all_orders()
    elif choice == "0":
        print("Thank you for exploring Zesty Zomato. See you soon...")
        break
    else:
        print("Invalid choice. Please try again") 
