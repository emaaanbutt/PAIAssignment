class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      return 100

  def make_purchase(self, quantity):
    try:
        if quantity > self.amount:
            raise ValueError("There are not enough items in the stock,sorry you cannot purchase")
        elif quantity < 0:
            raise ValueError("The quantity to be purchased should be positive")
         
        totalPrice = self.get_price(quantity)
        print(f"You have successfully purchased the items, Total price is: ${totalPrice:.3f}")

        self.amount= self.amount-quantity  # for showing remaining amount of stock
        print(f"Remaining stock: {self.amount}")
        
    except ValueError as e:
            print(f"Error: {e}")
        



      

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase
