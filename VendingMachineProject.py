import pickle
import streamlit as st
from PIL import Image

vend_pic=Image.open("vending machine.avif")
st.image(vend_pic, width=800)
available_products={"drinks":
                        {"drink1":"Dr. Pepper",
                         "drink2":"Coke",
                         "drink3":"Diet Coke",
                         "drink4":"Coke Zero",
                         "drink5":"Sprite",
                         "drink6":"Orange Fanta",
                         "drink7":"Grape Fanta",
                         "drink8":"Water",
                         "drink9":"Monster Ultra White",
                         "drink10":"Cold Brew Coffee"},
                    "snacks":
                        {"snack1":"Skittles",
                         "snack2":"Nutty Buddy",
                         "snack3":"M&M's",
                         "snack4":"Peanut M&M's",
                         "snack5":"Doritos",
                         "snack6":"Cheetos",
                         "snack7":"Lay's Classic",
                         "snack8":"Reese's",
                         "snack9":"Cheez-Its",
                         "snack10":"Granola Bar"}
                    }

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

    def add_product(self, Product):
        name=input("Enter product name: ")
        for i in available_products:
            if i != name:
                print("Please enter the name of an available product!")
                print(available_products)
        quantity=int(input("Enter quantity: "))
        if quantity>10:
            print("The maximum quantity is 10")
        price=input("Enter price: ")
        location=input("Enter the coordinate of the item: ")
        self.products.append(name)
        self.products.append(quantity)
        self.products.append(price)
        self.products.append(location)

    def display_products(self):
        for i in self.products:
            print(i)

    def purchase(self):
        letter=input("Enter the letter: ")
        number=input("Enter the number: ")
        combo=letter+number
        print (combo)
# take out money
# Purchase
# stock report
# empty machine

#--

while True:
    print("1. Enter user mode")
    print("2. Enter Vendor mode")
    choice=input("Enter Choice: ")

    if choice=="1":
        VendingMachine().display_products()
        file1=open("VendingMachine.dat", "rb")
        while True:
            try:
                data=pickle.load(file1)
                print(data.products)
                print(data.cash)
            except EOFError:
                break
            file1.close()

    if choice=="2":
        print("1. Add product")
        d1=input("Enter Choice: ")

        if d1=="1":
            VendingMachine().add_product(Product())
            file1=open("VendingMachine.dat", "ab")
            pickle.dump(VendingMachine, file1)
            file1.close()

        elif d1 == "2":
            VendingMachine().display_products()

        elif d1 == "3":
            print("Counting cash...")
            print()

        elif d1 == "4":
            exit()

        else:
            print("Invalid option")

    else:
        print("Invalid option")