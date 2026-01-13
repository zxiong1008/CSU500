def main():
    # Ask the user for the number of books purchased
    books_purchased = int(input("Enter the number of books purchased this month: "))

    # Determine points based on the number of books
    if books_purchased < 2:
        points = 0
    elif books_purchased < 4:
        points = 5
    elif books_purchased < 6:
        points = 15
    elif books_purchased < 8:
        points = 30
    else:
        points = 60

    # Display the results
    print(f"Books purchased: {books_purchased}")
    print(f"Points awarded: {points}")

if __name__ == "__main__":
    main()