"""
This script initializes InputHandling, PersonFactory, Adult and Child class.

Usage:
    python method_override.py


This script is a demonstration of OOP Classes, particularly inheritance.
The Child class is a subclass of the Adult one, thus inheriting its attributes.
The method can_drive is overridden in the Child class and prints that the child
is too young to drive.

"""


class InputHandling:
    """
    Utility class for handling user inputs, specifically for creating new instances of Adult or Child.
    This class provides methods for prompting the user for input and validating it.
    """

    @staticmethod
    def get_name():
        """
        Prompts the user to enter their name and validates the input.
        The method continues to prompt until the user enters a valid name
        consisting entirely of alphabetic characters.

        :return: The user's name as a string.
        :rtype: str
        """
        while True:
            name = input("Please enter your name: ")
            if name.isalpha():
                return name
            else:
                print("Ensure you enter your name correctly.")

    @staticmethod
    def get_age():
        """
        Prompts the user to enter their age and validates the input.
        This static method continues to prompt until the user enters an age greater than 0.
        It handles `ValueError` exceptions, which occur when the input cannot be converted to an integer,
        ensuring that only valid ages are accepted.

        :return: The user's age as an integer.
        :rtype: int
        """
        while True:
            try:
                age = int(input("Please enter your age: "))
                if age > 0:
                    return age
                else:
                    print("Please ensure you enter a number more than 0")
            except ValueError:
                print("Please ensure you enter a digit to represent your age.")

    @staticmethod
    def get_hair_colour():
        """
        Prompts the user to enter their hair colour and validates the input.
        The method continues to prompt until the user enters a valid hair colour
        consisting entirely of alphabetic characters.

        :return: The user's hair colour as a string.
        :rtype: str
        """
        while True:
            hair = input("Please type in your hair colour: ")
            if hair.isalpha():
                return hair
            else:
                print("Ensure you type in your hair colour correctly.")

    @staticmethod
    def get_eye_colour():
        """
        Prompts the user to enter their eye colour and validates the input.
        The method continues to prompt until the user enters a valid eye colour
        consisting entirely of alphabetic characters.

        :return: The user's eye colour as a string.
        :rtype: str
        """
        while True:
            eye = input("Please type in your eye colour: ")
            if eye.isalpha():
                return eye
            else:
                print("Ensure you type in your eye colour correctly.")


class PersonFactory:
    """
    This class uses the static method to create an instance of an Adult or Child
    based on the provided age. It does not rely on any instance specific data.
    """

    @staticmethod
    def create_user_type(name, age, hair_colour, eye_colour):
        """
        Creates and returns an instance of Adult or Child based on the provided age.

        This method uses the age to determine if the person is an adult
        or a child by calling the is_adult method of the Adult class.

        :param name: The name of the person.
        :type name: str
        :param age: The age of the person.
        :type age: int
        :param hair_colour: The hair colour of the person.
        :type hair_colour: str
        :param eye_colour: The eye colour of the person.
        :type eye_colour: str
        :return: An instance of Adult or Child based on the age.
        :rtype: Adult or Child
        """
        if Adult.is_adult(age):
            return Adult(name, age, hair_colour, eye_colour)
        else:
            return Child(name, age, hair_colour, eye_colour)


class Adult:
    """
    Parent class in the script.

    Attributes:
        name (str), age (int), hair colour (str), and eye colour (str)

    """

    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    @staticmethod
    def is_adult(age):
        """
        Static method used to determine if a person is an adult based on their age.

        :param age: The age of the person.
        :type age: int
        :return: `True` if the age is 18 or older, indicating the person is an adult; otherwise, `False`.
        :rtype: bool
        """
        return age >= 18

    def can_drive(self):
        """
        Prints a message indicating that the Adult instance object is able to drive.

        This method does not return a value; it simply prints a message to the console.
        """
        print(f"Woohoo, {self.name} is able to drive.")


class Child(Adult):
    """
    Subclass of Adult, representing a child.

    Inherits attributes and methods from the Adult class,
    with the ability to override or extend these behaviors as needed.
    This class introduces no additional attributes or methods beyond those inherited from Adult.
    """

    def __init__(self, name, age, hair_colour, eye_colour):
        """
        Initializes a Child instance with the given attributes.

        Calls the superclass's __init__ method to initialize the inherited attributes.

        :param name: The name of the child.
        :type name: str
        :param age: The age of the child.
        :type age: int
        :param hair_colour: The hair colour of the child.
        :type hair_colour: str
        :param eye_colour: The eye colour of the child.
        :type eye_colour: str
        """
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        """
        Overrides the can_drive method from the Adult class.
        This method prints a message indicating that the Child instance object is unable to drive.

        Method overriding is used here to provide a specific implementation
        of the can_drive method for the Child class, which differs from the Adult class.

        This method does not return a value; it simply prints a message to the console.
        """
        print(f"Unfortunately, {self.name} is too young to drive.")


def main():
    """
    Having a main method prevents the script from executing when imported as a module.
    """
    # Variables to store user data which is subsequently called on.
    user_name = InputHandling.get_name()
    user_age = InputHandling.get_age()
    user_hair_colour = InputHandling.get_hair_colour()
    user_eye_colour = InputHandling.get_eye_colour()

    # Calling on this creates an instance of either an Adult or Child class.
    person = PersonFactory.create_user_type(user_name, user_age, user_hair_colour, user_eye_colour)

    # Printing instance object attributes
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Hair Colour: {person.hair_colour}")
    print(f"Eye Colour: {person.eye_colour}")

    # Printing instance objects ability to be able to drive or not.
    person.can_drive()


if __name__ == "__main__":
    main()
