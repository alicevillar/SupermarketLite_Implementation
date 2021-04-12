
# Creating class Products with 3 attributes: name, product_id, category
class Products:
    def __init__(self, name, product_id, category):
        self.name = name
        self.product_id = product_id
        self.category = category

    # Function to create a method display
    def Display(self):
        print("Name:", self.name, "Product Id:", self.product_id, "Category:", self.category)
