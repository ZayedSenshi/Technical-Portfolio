# Initialize variable 'n' to value of 9.
# Initialize variable 'middle' by dividing 'n' by 2, to identify an upper half and lower half.
# Create a for loop with range 'n'.
# Use an if statement to check if iteration is < middle.
# Print middle lines with '*' with a length of (i + 1) to asterisks by 1.
# else statement prints lower half when 'i' is not < middle to decrement asterisks by 1.
# Overall upper half increases '*' whereas lower half decreases '*'.

n = 9
middle = n // 2
for i in range(n):
    if i < middle:
        print("*" * (i + 1))
    else:
        print("*" * (n - i))
