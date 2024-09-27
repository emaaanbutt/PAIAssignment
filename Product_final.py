# SP23-BAI-014 Eman Butt
# SP23-BAI-019 Ayesha Tahir
class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      try:
          if quantity <= 0:
              raise ValueError("Quantity must be a positive integer.")
          price = self.price * quantity
          if 0 < quantity < 10:
            return price
          elif 10 <= quantity <= 99:
            discount = 0.1 * price
            return price - discount
          elif quantity >= 100:
            discount = 0.2 * price
            return price - discount
      except ValueError as e:
          print(f"Error : {e}")
          return None

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
        

myProduct = Product("Book", 200, 1200)
myProduct.make_purchase(4)
myProduct.make_purchase(15)
myProduct.make_purchase(25)
myProduct.make_purchase(100)
myProduct.make_purchase(500)

print()

myProduct2 = Product("Mobile", 50, 10000)
myProduct2.make_purchase(60)
myProduct2.make_purchase(30)
myProduct2.make_purchase(-8)