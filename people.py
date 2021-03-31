# Creating superclass People with 6 attributes and 1 method
class People:
    # Function to create 6 attributes
    def __init__(self, name, id, phone, address, username, password):
        self.name = name
        self.id = id
        self.phone = phone
        self.address = address
        self.username = username
        self.password = password

# Function to create 1 method: checking password
    def checkpassword(self, password):
        if password == self.password:
            print("Correct password")
        else:
            print("Incorrect password! Try again")

