
import random

# Database
users = []
food_items = []
orders = []

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.user_id = random.randint(1000, 9999)  # Generate a random user ID
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
    
class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(10000, 99999)  # Generate a random food ID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Order:
    def __init__(self, user_id, food_item_ids, total_price):
        self.order_id = random.randint(100000, 999999)  
        self.user_id = user_id
        self.food_item_ids = food_item_ids
        self.total_price = total_price

# Admin Functionality
def add_food_item():
    name = input("Enter food item name: ")
    quantity = input("Enter quantity: ")
    price = float(input("Enter price: "))
    discount = float(input("Enter discount: "))
    stock = int(input("Enter stock amount: "))
    food_item = FoodItem(name, quantity, price, discount, stock)
    food_items.append(food_item)
    print("Food item added successfully!")

def edit_food_item():
    food_id = int(input("Enter food item ID: "))
    food_item = find_food_item_by_id(food_id)
    if food_item:
        food_item.name = input("Enter new name: ")
        food_item.quantity = input("Enter new quantity: ")
        food_item.price = float(input("Enter new price: "))
        food_item.discount = float(input("Enter new discount: "))
        food_item.stock = int(input("Enter new stock amount: "))
        print("Food item updated successfully!")
    else:
        print("Food item not found!")

def view_food_items():
    if len(food_items) > 0:
        for item in food_items:
            print(f"ID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
    else:
        print("No food items available.")

def remove_food_item():
    food_id = int(input("Enter food item ID: "))
    food_item = find_food_item_by_id(food_id)
    if food_item:
        food_items.remove(food_item)
        print("Food item removed successfully!")
    else:
        print("Food item not found!")

# User Functionality
def register_user():
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    password = input("Enter password: ")
    user = User(full_name, phone_number, email, address, password)
    users.append(user)
    print("User registered successfully!")

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = find_user_by_email(email)
    if user and user.password == password:
        print("Login successful!")
        show_user_menu(user)
    else:
        print("Invalid email or password.")

def place_new_order(user):
    view_food_items()
    selected_items = input("Enter the numbers of food items you want to order (comma-separated): ")
    selected_ids = [int(id) for id in selected_items.split(",")]
    order_items = []
    total_price = 0
    for food_id in selected_ids:
        food_item = find_food_item_by_id(food_id)
        if food_item:
            order_items.append(food_item)
            total_price += (food_item.price - (food_item.price * food_item.discount / 100))
    if len(order_items) > 0:
        order = Order(user.user_id, selected_ids, total_price)
        orders.append(order)
        print("Order placed successfully!")
    else:
        print("No items selected for order.")

def view_order_history(user):
    user_orders = find_orders_by_user_id(user.user_id)
    for order in user_orders:
        print(f"Order ID: {order.order_id}, Food Item IDs: {order.food_item_ids}, Total Price: {order.total_price}")

def update_profile(user):
    full_name = input("Enter new full name: ")
    phone_number = input("Enter new phone number: ")
    address = input("Enter new address: ")
    user.full_name = full_name
    user.phone_number = phone_number
    user.address = address
    print("Profile updated successfully!")

# Helper Functions
def find_food_item_by_id(food_id):
    for item in food_items:
        if item.food_id == food_id:
            return item
    return None

def find_user_by_email(email):
    for user in users:
        if user.email == email:
            return user
    return None

def find_orders_by_user_id(user_id):
    user_orders = []
    for order in orders:
        if order.user_id == user_id:
            user_orders.append(order)
    return user_orders

# Menu Functions
def show_admin_menu():
    print("------- Admin Menu -------")
    print("1) Add new food item")
    print("2) Edit the food item")
    print("3) View the food items")
    print("4) Remove the food item")
    print("--------------------------")

def show_user_menu(user):
    print("------- User Menu --------")
    print("1) Place new order")
    print("2) Order history")
    print("3) Update profile")
    print("4) Logout")
    print("--------------------------")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        place_new_order(user)
    elif choice == 2:
        view_order_history(user)
    elif choice == 3:
        update_profile(user)
    elif choice == 4:
        print("Logged out successfully!")
        return
    else:
        print("Invalid choice!")

# Main Program
def main():
    while True:
        print("------- Food Ordering App -------")
        print("1) Admin Login")
        print("2) User Login")
        print("3) User Registration")
        print("4) Exit")
        print("---------------------------------")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin_password = input("Enter admin password: ")  
            if admin_password == "admin_user":  
                show_admin_menu()
                admin_choice = int(input("Enter your choice: "))
                if admin_choice == 1:
                    add_food_item()
                elif admin_choice == 2:
                    edit_food_item()
                elif admin_choice == 3:
                    view_food_items()
                elif admin_choice == 4:
                    remove_food_item()
                else:
                    print("Invalid choice!")
            else:
                print("Invalid admin password.")
        elif choice == 2:
            login()
        elif choice == 3:
            register_user()
        elif choice == 4:
            print("Thank you for using the Food Ordering App!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

