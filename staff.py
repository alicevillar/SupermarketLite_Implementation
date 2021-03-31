# Creating class Staff - (inherits from People) + salary, position
from people import People

class Staff(People):
    # Function to create class with 8 attributes
    def __init__(self, name, id, phone, address, username, password, salary, position):
        People.__init__(self, name, id, phone, address, username, password)
        self.salary = salary
        self.position = position

    # Function to create a method display
    def Display(self):
        print("Name:", self.name, "Id:", self.id, "Phone:", self.phone, "Address:", self.address, "Username:",
              self.username, "Password:", self.password, "Salary:", self.salary, "Position", self.position, )

