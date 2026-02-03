class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                found = True
                # Only modify if values are not default
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print()
        print(f"Total: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    
    command = ""
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n").lower()
        
        if command == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, qty, desc))
            
        elif command == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
            
        elif command == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            # Creating a dummy object with default price/desc as per requirements
            new_item = ItemToPurchase(item_name=name, item_quantity=qty)
            cart.modify_item(new_item)
            
        elif command == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            
        elif command == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

def main():
    # Step 7: Initial Input
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    # Initialize the Cart
    my_cart = ShoppingCart(customer_name, current_date)
    
    # Step 5: Start the menu loop
    print_menu(my_cart)

if __name__ == "__main__":
    main()