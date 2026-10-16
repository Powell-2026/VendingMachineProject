class Product(object):
    def __init__(self):
        self.name = ""
        self.quantity = ""
        self.price = ""
class VendingMachine(object):
    def __init__(self):
        self.products = []
        self.cash= ""
    def add_product(self, product):
