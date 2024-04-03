# Prompt the user to input three whole numbers and convert them to integers
numbers = [int(input("Please type in a whole number: ")) for _ in range(3)]

first_number = numbers[0]
second_number = numbers[1]
third_number = numbers[2]

first_result = sum(numbers)
print(first_result)

second_result = first_number - second_number
print(second_result)

third_result = third_number * first_number
print(third_result)

fourth_result = sum(numbers) / third_number
print(fourth_result)