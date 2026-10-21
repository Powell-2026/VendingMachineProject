class Product(object):
    def __init__(self):
        self.name = ""
        self.quantity = ""
        self.price = ""
        self.location = ""
class VendingMachine(object):
    def __init__(self):
        self.products = []
        self.cash= ""
    def add_product(self, product):
        name=input("Enter product name: ")
        quantity=input("Enter quantity: ")
        if quantity>10:
            print("The maximum quantity is 10")
        price=input("Enter price: ")
        location=input("Enter the coordinate of the item: ")
        self.products.append(name)
        self.products.append(quantity)
        self.products.append(price)
        self.products.append(location)
    def display_products(self):
        i=1
        while True:
            print(self.products[i])
            i=i+1
            if i>6:
                break
#--
while True:
    print("1. Enter user mode")
    print("2. Enter Vendor mode")
    choice=input()
    if choice=="1":
        VendingMachine().display_products()
    if choice=="2":
        print("1. Add product")
        d1=input()
        if d1=="1":
            VendingMachine().add_product(Product())