''' Iterations is the process of executing a set of instructions or block of code.
They are usually associated with loops where the same block of code is executed mutiple times
either for a specified number of times or until a condition is met/
Iterations avoid writing code again unecessarily. The computer does it for us

While loops control flow structures that repeatedly execute of block of code as long as a
specificed condition is true. They continue iterating as long as the condition becomes false

For loops are used when you know the number of times you want to execute a block of code

'''
#initialized variable 'count' with a value of 0
#while loop checks if count is less than 5. Since it is, the loop begins
#print function is used inside the loop to print out the current value of count
#the count variable is then incremented by 1 using the += operator
#loop repeats until count is no longer less than 5 as the condition is now met
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

#'pokemon' refers to the items in the list. Hence when it is printed, each pokemon is printed
pokemon_list = ["Pikachu", "Charizard", "Squirtle", "Slowpoke"]
for pokemon in pokemon_list:
    print(pokemon)