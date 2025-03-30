def run():
    # Main execution function that ties everything together
    print("Running the program...")

    # Define a Product class to represent items in the store
    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price # Price per unit (or per kg)

    # Define a ShoppingCart class to manage products
    class ShoppingCart: 
        def __init__(self):
            self.cart = {} # Dictionary to store products and their quantities
        
        # Method to add a product to the cart
        def add_product(self, product, quantity=1):
            print()
            self.cart.update({product.name: {"product": product,
                                        "quantity": quantity}})
            print(f"{quantity}kg {product.name} is added to cart!!!")
            
        def remove_product(self, product, quantity=1):
            print()
            # Remove the entire product entry if quantity is equal or greater than existing
            if quantity >= self.cart[product.name]['quantity']:
                item = self.cart.pop(f'{product.name}')
                print(f"{product.name} is removed from the cart!!!")
            else:
                # Reduce the quantity of the product in the cart
                self.cart[product.name]['quantity'] -= quantity
                print(f"{quantity}kg of {product.name} is removed from the cart!!!")

        # Method to display the current cart contents and the total calculated cart
        def display_cart(self):
            print()
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

    # Create products
    apple = Product("Apple", 0.99)
    banana = Product("Banana", 0.59)
    milk = Product("Milk", 3.49)

    # Create cart
    cart = ShoppingCart()

    # Add items
    cart.add_product(apple, 3)
    cart.add_product(banana)
    cart.add_product(milk, 2)
    cart.display_cart()

    # Remove items
    cart.remove_product(apple, 1)
    cart.remove_product(banana)
    cart.display_cart()

    # Try to remove a product not in the cart
    cart.remove_product(milk, 5)  # Removes all milk
    cart.display_cart()

if __name__ == '__main__':
    # This will execute when the script is run directly
    run()