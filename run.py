def run():
    # Main execution function that ties everything together
    print("Running the program...")

    # Your code here
    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class ShoppingCart: 
        def __init__(self):
            self.cart = {}
        
        def add_product(self, product, quantity=1):
            print()
            self.cart.update({product.name: {"product": product,
                                        "quantity": quantity}})
            print(f"{quantity}kg {product.name} is added to cart!!!")
            
        def remove_product(self, product, quantity=1):
            print()
            if quantity >= self.cart[product.name]['quantity']:
                item = self.cart.pop(f'{product.name}')
                print(f"{product.name} is removed from the cart!!!")
            else:
                self.cart[product.name]['quantity'] -= quantity
                print(f"{quantity}kg of {product.name} is removed from the cart!!!")

        def display_cart(self):
            items = self.cart.items()
            for i, item in enumerate(items):
                print(f'{i}  {item[0]}  {item[1]['product'].price}  {item[1]['quantity']}kg')
            print(f'Total: {self.calculate_total()} Euros')

        def calculate_total(self):
            print()
            total = 0
            for product in self.cart.keys():
                price = self.cart[product]['product'].price
                quantity = self.cart[product]['quantity']
                total += price*quantity
            return total
        
    apple = Product("Apple", 0.99)
    banana = Product("Banana", 0.59)
    milk = Product("Milk", 3.49)

    cart = ShoppingCart()
    cart.add_product(apple, 3)
    cart.add_product(banana)
    cart.add_product(milk, 2)
    cart.remove_product(apple, 1)
    cart.remove_product(banana)
    print()
    cart.display_cart()

if __name__ == '__main__':
    # This will execute when the script is run directly
    run()