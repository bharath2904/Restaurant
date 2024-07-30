# Simple method to order burger and drinks
import random
class Order:
    def __init__(self):
        self.size_options = ["regular", "large", "special"]
        self.drink_options = ["coke", "sprite", "icedcoke", "icecream", "hottea", "hotchocolate"]
        
    def book(self):
        print("Choose size from the following options:", self.size_options)
        size = input("Enter your choice: ").strip().lower()
        if size in self.size_options:
            print("Added to order")
        else:
            print(f"{size} is not a valid option.")
            self.pay()
    
    def pay(self):
        print("Payment options:")
        print("1. Pay at counter")
        print("2. Mobile Payment")
        choice = input("Choose payment method (1 or 2): ").strip()
        if choice == '1':
            print("Pay at counter")
            generate_bill_number()
            
        elif choice == '2':
            print("Mobile Payment")
           
        else:
            print("Invalid choice. Please choose 1 or 2.")
            self.book()

def generate_bill_number():
            number = random.randint(1, 50)
            print("Your bill number is:",number)
           
            

def welcome():
    print("Welcome to the HOUSE OF BURGER AND DRINKS!")
    burger_selection()

def burger_selection():
    burger_types = ["veg", "non veg"]
    print("Available burger types:", burger_types)
    choice = input("Please enter your burger type (veg/non veg): ").strip().lower()
    if choice == "veg":
        veg_burger()
    elif choice == "non veg":
        non_veg_burger()
    else:
        print(f"{choice} is not a valid option.")
        burger_selection()

def veg_burger():
    veg_options = ["paneer", "cheese", "chinese", "vegetables", "healthy", "pav bhaji"]
    print("Available veg burgers:", veg_options)
    choice = input("Choose your veg burger: ").strip().lower()
    if choice in veg_options:
        print(f"{choice} is available.")
        order = Order()
        order.book()
        soft_drinks()
    else:
        print(f"{choice} is not available. Please choose from the list.")
        veg_burger()

def non_veg_burger():
    non_veg_options = ["chicken", "mutton", "friedchicken", "beef"]
    print("Available non-veg burgers:", non_veg_options)
    choice = input("Choose your non-veg burger: ").strip().lower()
    if choice in non_veg_options:
        print(f"{choice} is available.")
        order = Order()
        order.book()
        soft_drinks()
    else:
        print(f"{choice} is not available. Please choose from the list.")
        non_veg_burger()

def soft_drinks():
    print("Available drinks:", Order().drink_options)
    choice = input("Please enter your drink choice: ").strip().lower()
    if choice in Order().drink_options:
        print(f"{choice} is available.")
        order = Order()
        order.pay()
        thanks()
    else:
        print(f"{choice} is not available.")
        soft_drinks()

def thanks():
    print("Enjoy your day!!! Thank you for visiting.")
    
welcome()

