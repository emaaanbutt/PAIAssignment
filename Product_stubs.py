class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      price = self.price * quantity
      if 0 < quantity < 10:
          return price
      elif 10 <= quantity <= 99:
          discount = 0.1 * price
          return price - discount
      elif quantity >= 100:
          discount = 0.2 * price
          return price - discount
          
  def make_purchase(self, quantity):
      pass

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase
