def main():
    # Get current time and wait duration from the user
    current_time = int(input("What is the current time (in hours, 0-23)? "))
    wait_hours = int(input("How many hours do you want to wait? "))

    # Calculate the final time
    # Adding the wait time to the current time, then finding the remainder when divided by 24
    alarm_time = (current_time + wait_hours) % 24

    # Output the result
    print(f"The alarm will go off at {alarm_time}")

# This check ensures the main() function only runs if this 
# specific file is executed (not if it's imported elsewhere)
if __name__ == "__main__":
    main()