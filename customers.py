
# Creating class Customers - (inherits from People) + purchaseHistory
from people import People

class Customers(People):
    def __init__(self, name, id, phone, address, username, password, purchaseHistory):
        People.__init__(self, name, id, phone, address, username, password)  # inheritance from class People
        self.purchasehistory = purchaseHistory

    # Function to create a method display
    def Display(self):
        print("Name:", self.name, "Id:", self.id, "Phone:", self.phone, "Address:", self.address, "Username:",
              self.username, "Password:", self.password, "PurchaseHistory:", self.purchasehistory)

