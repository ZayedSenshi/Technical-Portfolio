'''
sum1 = 0 # Initialize sum1 to 0
i = 2     # Initialize i to 2

# While loop that continues as long as sum1 is less than or equal to 250
while sum1 <= 250:
    sum1 += i # Add the value of i to sum1
    i += 2      # Increment i by 2 for the next iteration
    print(sum1) # Print the current value of sum1


#intitialize variable 'my_number' to 0. Loop runs until 'my number' is less than 100. Special condition 'break' used to stop loop when it reaches 23
my_number = 0

while my_number < 100:
    my_number += 1
    print(my_number)
    if my_number == 23:
        break


my_number = 0

while my_number < 100:
    my_number += 1
    if my_number > 23:
        continue
    print(my_number)
'''
#first time the loop runs i = 1 and it prints i. Then on the second iteration i = 2 and two will print. This goes up to, but excluding 10, so will print 1-9. 'i' is the index variable so it tells you the iteration the loop is on. In each iteration, the indented code is repeated
# for i in range(1, 10):
#     if i > 5:
#         print(i)

# for i in range(1, 4):
#     print("i: ", i)
#     for j in range(1, 4):
#         print("j: ", j)
#         print(i * j, end=" ")
#         print("i * j", i * j)
#     print()

# for i in range(1, 4):
#    for j in range(1, 4):
#        print(i * j, end=" ")
#    print()

# for i in range(1 , 5):
#     for j in range (1, 5):
#         print(i * j, end=" ")
while True:
    odd_height = int(input("Please enter an odd number: "))
    if odd_height % 2 != 0:
        break
    else:
        print("That's not an odd number")
