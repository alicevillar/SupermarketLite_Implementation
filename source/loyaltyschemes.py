# Creating class LoyatySchemes with 2 attributes:id, total
class LoyaltySchemes:
    def __init__(self, loyalty_id, total):
        self.id_loyalty = loyalty_id
        self.total = total

# Function to create a method display
    def Display(self):
        print("Id:", self.id_loyalty, "Total:", self.total)