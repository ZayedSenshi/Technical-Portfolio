# class Student:
#     def __init__(self, age, name, gender, grades):
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.grades = grades
#
#     def compute_average(self):
#         average = sum(self.grades) // len(self.grades)
#         print("The average grade for student " + self.name + " is " + str(average))
#
# mario = Student(26, "Mario Foli", "Male", [64, 70])
# lisa = Student(18, "Lisa Powell", "Female", [90, 58, 70])
#
# mario.compute_average()

class Wolf:
    classification = "canine"
    habitat = "forest"
    is_sleeping = False # Defaults to being awake initially

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_sleeping_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake!"
        else:
            return self.name + " is sleeping."


silver_tooth = Wolf("Silvertooth", 5)
print(silver_tooth.show_sleeping_state())

silver_tooth.is_sleeping = True
print(silver_tooth.show_sleeping_state())