def main():
    # Get the number of years from the user
    num_years = int(input("Enter the number of years: "))

    total_rainfall = 0.0
    
    # Outer loop for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        print("----------")
        
        # Inner loop for each of the 12 months
        for month in range(1, 13):
            # Collect rainfall for the specific month
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_rainfall += rainfall

    # Calculate final statistics
    total_months = num_years * 12
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\n--- Final Results ---")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()