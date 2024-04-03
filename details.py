#uses variables to store user information
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))
user_house_number = (input("Please enter your house number: "))
user_street_name = input("Please enter your street name: ")
#prints user information in a sentence using an f-string
print(f"This is {user_name}. He is {user_age} years old and lives at house number {user_house_number} on {user_street_name}.")