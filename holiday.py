# Global variables allowing access outside of functions.

cities = {
    "a": "Amsterdam (Netherlands)",
    "b": "Lagos (Nigeria)",
    "c": "Montego Bay (Jamaica)"
}
# value key for key value iterates over dictionary.items and reverses order.
city_code_mapping = {v: k for k, v in cities.items()}

daily_hotel_costs = {
    "a": 100,  # Cost for Amsterdam
    "b": 150,  # Cost for Lagos
    "c": 200  # Cost for Montego Bay
}

daily_flight_cost = {
    "a": 25,
    "b": 50,
    "c": 75
}

daily_rental_cost = {
    "a": 20,
    "b": 30,
    "c": 40
}


def get_city_flight():
    while True:

        # Responsible for printing the block by iterating over the dictionary
        # and printing the keys and values - effectively prints the dictionary.
        print("Please choose from the following cities to fly to:")
        for key, city in cities.items():
            print(f"{key}) {city}")

        # gets the user's choice. Must use [city_flight] as a way of accessing key
        # city_flight stores the user's choice which corresponds to the key of cities
        city_flight = input("I want to go to: ").lower()
        if city_flight in cities:
            # selected_city stores the value of the user input in comparison to the dict.
            selected_city = cities[city_flight]
            print(f"You have chosen to fly to {selected_city}.\n"

                  f"The daily hotel cost is: £{daily_hotel_costs[city_flight]}.\n"
                  f"The daily flight cost is: £{daily_flight_cost[city_flight]}.\n"
                  f"Should you choose to rent a car, "
                  f"the daily car rental cost is: £{daily_rental_cost[city_flight]}.")
            return selected_city
        else:
            print("You did not enter either 'a', 'b' or 'c'")


def get_num_nights():
    while True:
        try:
            num_nights = int(input("Please enter the number of nights you will be staying: "))
            if num_nights < 1:
                print("Ensure you enter at least 1.")
            else:
                return num_nights
        except ValueError:
            print("Oops, remember to type in a whole number.")


def get_rental_days(num_nights_staying):
    while True:
        try:
            rental_days = int(input("Please enter the number of days you'd like to rent a car: "))
            if rental_days > num_nights_staying or rental_days < 0:
                print("Ensure that you enter at a minimum of 0, or, "
                      "less than or equal to the number of nights you are staying.")
            else:
                return rental_days
        except ValueError:
            print("Oops. Remember to type in a whole number.")


def hotel_cost(city_flight, num_nights_staying, daily_hotel_costs):
    total_hotel_cost = daily_hotel_costs[city_flight] * num_nights_staying
    return total_hotel_cost


def plane_cost(city_flight, daily_flight_cost, num_nights_staying):
    total_plane_cost = daily_flight_cost[city_flight] * num_nights_staying
    return total_plane_cost


def car_rental(city_flight, daily_rental_cost, num_rental_days):
    total_rental_cost = daily_rental_cost[city_flight] * num_rental_days
    return total_rental_cost


def holiday_cost():
    total_holiday_cost = cost_of_hotel + cost_of_plane + cost_of_rental
    print(f"\033[1mThe entire cost of your holiday is £{total_holiday_cost}\033[0m")
    return total_holiday_cost


city_to_fly_to = get_city_flight()
city_code = city_code_mapping[city_to_fly_to]

num_nights_staying = get_num_nights()
print(f"You have decided to stay for {num_nights_staying} nights.")

num_rental_days = get_rental_days(num_nights_staying)
print(f"You are renting a car for {num_rental_days} days.")

# Using city_code as an argument to access the key that the user has chosen
cost_of_hotel = hotel_cost(city_code, num_nights_staying, daily_hotel_costs)
print(f"The total cost of your hotel is: £{cost_of_hotel}.")

cost_of_plane = plane_cost(city_code, daily_flight_cost, num_nights_staying)
print(f"The total cost of your flight is: £{cost_of_plane}.")

cost_of_rental = car_rental(city_code, daily_rental_cost, num_rental_days)
print(f"The total cost of your car rental is: £{cost_of_rental}.")

cost_of_holiday = holiday_cost()
