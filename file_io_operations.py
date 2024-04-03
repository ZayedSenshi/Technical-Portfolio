# contents = ""
#
# with open('example.txt', 'r+') as file:
#     for line in file:
#         contents += line
#     print(contents)

def get_odd_number():
    while True:
        try:
            user_input = int(input("Please enter an odd number: "))
            if user_input % 2 != 0:
                return user_input
            else:
                print("That's not an odd number")
        except ValueError:
            print("Please ensure you enter a number!")
#
# user_input = get_odd_number()
#
# print(user_input)

name = input("Please write your name: ")

with open('output.txt', 'w') as f:
    f.write(name+"\n")
    f.write("My name is above!")