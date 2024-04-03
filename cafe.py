menu = ["Muffin", "Cake", "Sandwich", "Panini"]

stock = {"Muffin": 10,
         "Cake": 15,
         "Sandwich": 20,
         "Panini": 25}

price = {"Muffin": 5,
         "Cake": 7,
         "Sandwich": 9,
         "Panini": 11}

# for loop iterates through each key in menu.
# Stock and price contain the corresponding value, accessed by 'item'.
# Multiply stock by price to get total value for each item in menu.
# sum function adds it up neatly.
total_value = sum(stock[item] * price[item] for item in menu)


print(f"The total stock worth is: £{total_value}")
