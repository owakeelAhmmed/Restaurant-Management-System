from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("item not found")

    def view_cart(self):
        print("****View Menu****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")

class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items()) 
    
    def clear(self):
        self.items = {}

    def pay_bill(self):
        print(f"Total {self.total_price} paid successfully ")
        self.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employees(self, restaurent):
        restaurent.view_employees()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)
        
    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        print("List of Employees:")
        for emp in self.employees:
            print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, Address: {emp.address}")


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted!!")
        else:
            print("Item Not Found")

    def show_menu(self):
        print("********* Menu *********")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

my_restaurant = Restaurent("My Restaurant")

def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    addres = input("Enter Your Address : ")
    customer = Customer(name=name, email=email, phone = phone, address=addres)


    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")


        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            customer.view_menu(my_restaurant)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(my_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.cart.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    addres = input("Enter Your Address : ")
    admin = Admin(name=name, email=email, phone = phone, address=addres)


    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")


        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Iterm Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(my_restaurant, item)
        elif choice == 2:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone : ")
            address = input("Enter Address : ")
            age = int(input("Enter Age : "))
            designation = input("Enter Designation : ")
            salary = int(input("Enter Salary : "))
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(my_restaurant, employee)
        elif choice == 3:
            admin.view_employees(my_restaurant)
        elif choice == 4:
            admin.view_menu(my_restaurant)
        elif choice == 5:
            item_name = input("Enter Your Item Name : ")
            admin.remove_item(my_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


while True:
    print("*******Welcome*******")
    print("1.Customer")
    print("2 Admin")
    print("3 Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")