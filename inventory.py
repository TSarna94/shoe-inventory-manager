"""
===========================================================
Shoe Inventory Management System
Developer: Tony
Academic Honesty Statement:
This project represents my own work. I have not copied code
from any external source, nor have I allowed anyone else to
complete this work for me. Any assistance received was used
for learning and understanding, not for direct submission.
===========================================================
"""

# ========================= Imports =========================
# (None required, but section included for PEP-8 structure)


# ========================= Classes =========================
class Shoe:
    """
    Represents a shoe item in the inventory.

    Attributes:
        country (str): Country of origin.
        code (str): Unique shoe code.
        product (str): Product name.
        cost (int): Cost of the shoe.
        quantity (int): Quantity in stock.
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Return a formatted string representation of the shoe."""
        return (
            f"Shoe Details:\n"
            f"Country: {self.country}\n"
            f"Code: {self.code}\n"
            f"Product: {self.product}\n"
            f"Cost: {self.cost}\n"
            f"Quantity: {self.quantity}"
        )


# ========================= Global List =========================
shoe_list = []


# ========================= Helper Functions =========================
def update_inventory_file():
    """
    Rewrite the entire inventory file based on the current shoe_list.
    Ensures file stays in sync after restocking.
    """
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"Error updating inventory file: {e}")


# ========================= Main Functions =========================
def read_shoes_data():
    shoe_list.clear()  # prevents duplication
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
        print("Shoe data loaded successfully.")
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")

def capture_shoes():
    """
    Capture a new shoe from user input and append it to the inventory.
    Also writes the new shoe to the inventory file.
    """
    country = input("Enter the country of the shoe: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the product name: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    with open("inventory.txt", "a") as file:
        file.write(f"{country},{code},{product},{cost},{quantity}\n")

    print("Shoe captured and added to inventory.")


def view_all():
    """
    Display all shoes in the inventory using their __str__ method.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    print("\n========== All Shoes ==========")
    for shoe in shoe_list:
        print(shoe)
        print("-" * 30)


def re_stock():
    """
    Find the shoe with the lowest quantity and allow the user to restock it.
    Updates both the in-memory list and the inventory file.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    lowest_shoe = min(shoe_list, key=lambda s: s.quantity)
    print(f"Lowest stock item:\n{lowest_shoe}")

    choice = input("Would you like to restock this item? (yes/no): ").lower()
    if choice == "yes":
        restock_amount = int(input("Enter restock amount: "))
        lowest_shoe.quantity += restock_amount
        update_inventory_file()
        print(f"{lowest_shoe.product} restocked. New quantity: {lowest_shoe.quantity}")


def search_shoe():
    """
    Search for a shoe by its code and display it if found.
    """
    code = input("Enter the shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("\nShoe found:")
            print(shoe)
            return

    print("Shoe not found.")


def value_per_item():
    """
    Calculate and display the total value of each shoe item.
    Formula: value = cost * quantity
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    print("\n========== Value Per Item ==========")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: Total Value = {value}")


def highest_qty():
    """
    Display the shoe with the highest quantity and mark it as 'for sale'.
    """
    if not shoe_list:
        print("No shoes in inventory.")
        return

    highest_shoe = max(shoe_list, key=lambda s: s.quantity)
    print(f"Highest quantity item:\n{highest_shoe}")
    print("This shoe is for sale.")


#==========Main Menu=============
# ========================= Main Menu =========================
def main():
    """Main menu loop for the Shoe Inventory Management System."""
    read_shoes_data()

    while True:
        print("\n========== Shoe Inventory Management System ==========")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Restock Shoe")
        print("4. Search Shoe")
        print("5. Value Per Item")
        print("6. Highest Quantity Shoe")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
