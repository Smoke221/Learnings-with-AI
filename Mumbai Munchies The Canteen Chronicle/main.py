# Snack inventory dictionary to store snack details
snack_inventory = {}

# Sales records dictionary to store snack sales
sales_records = {}

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Is the snack available? (yes/no): ")

    snack_inventory[snack_id] = {
        "snack_name": snack_name,
        "price": price,
        "availability": availability.lower() == "yes"
    }
    print("Snack added to inventory successfully.")

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter snack ID to remove: ")
    if snack_id in snack_inventory:
        del snack_inventory[snack_id]
        print("Snack removed from inventory successfully.")
    else:
        print("Snack ID not found in inventory.")

# Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    if snack_id in snack_inventory:
        availability = input("Is the snack available now? (yes/no): ")
        snack_inventory[snack_id]["availability"] = availability.lower() == "yes"
        print("Snack availability updated successfully.")
    else:
        print("Snack ID not found in inventory.")

# Function to record a snack sale
def record_sale():
    snack_id = input("Enter snack ID sold: ")
    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["availability"]:
            if snack_id not in sales_records:
                sales_records[snack_id] = 1
            else:
                sales_records[snack_id] += 1
            snack_inventory[snack_id]["availability"] = False
            print("Sale recorded successfully.")
        else:
            print("Snack is currently unavailable.")
    else:
        print("Snack ID not found in inventory.")

# Function to display the current inventory
def display_inventory():
    print("Current Snack Inventory:")
    print("ID\tName\tPrice\tAvailability")
    for snack_id, snack_details in snack_inventory.items():
        print(
            f"{snack_id}\t{snack_details['snack_name']}\t{snack_details['price']}\t{'Yes' if snack_details['availability'] else 'No'}"
        )

# Function to display the sales records
def display_sales_records():
    print("Snack Sales Records:")
    print("ID\tName\tPrice\tQuantity")
    for snack_id, quantity in sales_records.items():
        snack_details = snack_inventory[snack_id]
        print(
            f"{snack_id}\t{snack_details['snack_name']}\t{snack_details['price']}\t{quantity}"
        )

# Function to display available snacks
def display_available_snacks():
    print("Available Snacks:")
    print("ID\tName\tPrice")
    for snack_id, snack_details in snack_inventory.items():
        if snack_details['availability']:
            print(
                f"{snack_id}\t{snack_details['snack_name']}\t{snack_details['price']}"
            )


# Main program loop
while True:
    print("\n*** Welcome to Mumbai Munchies ***")
    print("1. Add a snack to inventory")
    print("2. Remove a snack from inventory")
    print("3. Update snack availability")
    print("4. Record a snack sale")
    print("5. Display current inventory")
    print("6. Display snack sales records")
    print("7. Display available snacks")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        display_inventory()
    elif choice == "6":
        display_sales_records()
    elif choice == "7":
        display_available_snacks()
    elif choice == "0":
        print("Thank you for using Mumbai Munchies. Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
