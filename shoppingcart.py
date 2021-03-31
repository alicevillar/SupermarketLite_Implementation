# Creating class ShoppingCart with 3 attributes

class ShoppingCart:
    def __init__(self, shoppingcart_id, product_id, customer_id):
        self.shoppingcart_id = shoppingcart_id
        self.product_id = product_id
        self.customer_id = customer_id

    # Function to create a method display
    def Display(self):
        print("Shopping Cart Id:", self.shoppingcart_id, "Product Id:", self.product_id, "Customer Id:",
              self.customer_id)

