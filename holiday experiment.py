# Task: Calculate a user's total holiday cost
# Includes: 1) Plane cost 2) Hotel cost 3) Car-rental cost
# Use while loop to Create 3 options for a destination the user will fly to
# Use inner while loop to ask for number of nights


# Use a while loop to ascertain chosen destination and print a user-friendly message
while True:
    city_flight = input("""Please choose from the following cities to fly to: 
    a) Amsterdam,
    b) Nigeria,
    c) Jamaica
    I want to go to: """).lower()
    if city_flight in ("a", "b", "c"):
        if city_flight == "a":
            print("You have chosen to fly to Amsterdam!")
        elif city_flight == "b":
            print("You have chosen to fly to Nigeria!")
        elif city_flight == "c":
            print("You have chosen to fly to Jamaica!")

        while True: # Inner loop keeps asking for number of nights
            try:
                num_nights = int(input("Please enter the number of nights you'd like to stay: "))
                if num_nights < 1:
                    print("Please enter a number greater than 0.")
                else:
                    print(f"You will be staying for {num_nights} nights.")
                    break # Exit inner loop if number is valid
            except ValueError:
                print("Please enter a valid number.")

                while True: # Another loop to ask for rental cars
                    try:
                        rental_days = int(input("Please enter the number of days for which you will be hiring a car: "))
                        if rental_days < 1:
                            print("Please enter a number greater than 0.")
                        else:
                            print(f"You will be hiring a car for {rental_days} days.")
                            break # Exit nested loop if number is valid
                    except ValueError:
                        print("Please enter a valid number")

        break # Exit outer loop after valid number of nights is entered
    else:
        print("You did not enter either 'a','b' or 'c'")



