# Creating class Payment with 3 attributes
class Payment:
    def __init__(self, payment_id, shoppingcart_id, loyalty_id):
        self.payment_id = payment_id
        self.shoppingcart_id = shoppingcart_id
        self.loyalty_id = loyalty_id

    # Function to create a method display
    def Display(self):
        print("Payment Id:", self.payment_id, "Shopping Cart Id", self.shoppingcart_id, "Loyalty Id:", self.loyalty_id)

