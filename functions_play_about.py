import random
#     y = x / 2
#     return y
#
# my_value = divide_by_2(10)
# print(my_value)

# Define a function with a single variable 'x'

# def random_number(x):
#     # Calculation for random number * operator unpacks the tuple into 2 separate arguments
#     # for the random.randint function to work. This is stored in the random_number_result
#     random_number_result = random.randint(*x)
#     # Function returns random_number_result
#     return random_number_result
#
# # Use any variable to set the desired range.
# r = (-200, 1000)
# # Use another variable to utilise the function 'random_number' within the parameters of 'r'
# any_random = random_number(r)
# # print any_random variable which will give a random number between -200 and 1000
# print(any_random)


# def squared_number(x): # Naming of function with parameter x
#     squared_result = x * x # Calculation stored in variable by multiplying x by x
#     return squared_result # Returns value of squared_result which is the square of input x
#
# eight_squared = squared_number(8) # Function called with an argument of 8
# print(eight_squared) # Value is printed

# Define function 'sum_plus_two' with 3 parameters
def sum_plus_two(description, x, y):
    outcome = (x + 1) + (y + 1) # Calculation logic
    return description + str(outcome)

x_number = 56
y_number = 5
friendly_message = "The number you have calculated is: "

total_sum = sum_plus_two(friendly_message, x_number, y_number)
print(total_sum)
