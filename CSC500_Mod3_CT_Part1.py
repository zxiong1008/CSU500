# Constant rates for tax and tip
TIP_RATE = 0.18
TAX_RATE = 0.07

def main():
    # 1. Ask the user for the food charge
    try:
        food_charge = float(input("Enter the charge for the food: $"))

        # 2. Calculate tip and tax
        tip_amount = food_charge * TIP_RATE
        tax_amount = food_charge * TAX_RATE

        # 3. Calculate the grand total
        total_price = food_charge + tip_amount + tax_amount

        # 4. Display the results formatted to 2 decimal places
        print("\n--- Receipt ---")
        print(f"Food Charge: ${food_charge:,.2f}")
        print(f"Tip (18%):   ${tip_amount:,.2f}")
        print(f"Tax (7%):    ${tax_amount:,.2f}")
        print("----------------")
        print(f"Total Price: ${total_price:,.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a numerical value for the food charge.")

if __name__ == "__main__":
    main()