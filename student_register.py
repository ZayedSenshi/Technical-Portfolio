# Use a function to ensure user enters a positive number and nothing else.
# Create variable that calls on function and stores number of students.
# Create variable that stores student ID numbers.
# Use pythonic method to open file and for loop to gather id_numbers.
# Use write function to write data to the text file.
# Use f-string to embed each student id and \n to print each one on a new line.

def get_positive_integer():
    while True:
        try:
            user_input = int(input("Please enter the number of students registering for the exam: "))
            if user_input > 0:
                return user_input
            else:
                print("Please ensure you enter at least 1.")
        except ValueError:
            print("You have not entered a whole number. Please try again.")


students_registering = get_positive_integer()

id_number = [input("Please enter the student ID number: ")
             for student in range(students_registering)]

with open('reg_form.txt', 'w') as file:
    for id in id_number:
        file.write(f"Student ID: {id} Please sign...................\n")
