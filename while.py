# Initialize variables to keep track of total_sum and count_of_inputs.
# Use a while loop to repeatedly ask user to enter a number.
# Use try/except to handle errors.
# Inside loop, create a variable to store values of numbers user enters.
# Use an if statement as a means of breaking the loop if user enters -1.
# Use compound assignment operator to add numbers user entered to total_sum.
# Use compound assignment operator to increment the count of numbers entered.
# Outside loop, create a variable to store the average of numbers entered.
# Print average sum with a user-friendly message.

total_sum = 0
count = 0

while True:
    try:
        user_number = int(input("Please enter a number: "))
        if user_number == -1:
            break
        total_sum += user_number
        count += 1
    except ValueError:
        print("Ensure you enter a whole number.")

average = total_sum / count
print("The average of the numbers entered, excluding the -1, is:", average)
