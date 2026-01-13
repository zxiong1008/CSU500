class ItemToPurchase:
    # Step 1: Default constructor
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method to print the formatted cost
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        # Using f-strings for clean formatting
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

if __name__ == "__main__":
    # Step 2: Prompt for Item 1
    print("Item 1")
    name1 = input("Enter the item name:\n")
    price1 = float(input("Enter the item price:\n"))
    qty1 = int(input("Enter the item quantity:\n"))
    
    item1 = ItemToPurchase(name1, price1, qty1)
    print() # Adding a newline for spacing

    # Prompt for Item 2
    print("Item 2")
    name2 = input("Enter the item name:\n")
    price2 = float(input("Enter the item price:\n"))
    qty2 = int(input("Enter the item quantity:\n"))
    
    item2 = ItemToPurchase(name2, price2, qty2)
    
    # Step 3: Output the Total Cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost:.0f}")