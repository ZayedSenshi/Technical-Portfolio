
# Dictionaries can be defined with the curley brackets
# 'Key' is the common element whilst 'value' is individual
# Use the colon to signify that it is a pair
# Use commas to add more elements
# Dictionaries can be on separate lines as long as it contains commas and is enclosed in curley brackets.
# What you can do to a list you can do to a dictionary, barring append
# Can't index via normal indexing means
# Use the key to pull out values
# my_dictionary = {"Name": "Peter",
#                  "Age": "32",
#                  "Sex": "Male"}
# # Use the key to pull out values
# print(my_dictionary["Age"])
#
# # To access all keys in dictionary
# for i in my_dictionary.keys():
#     print(i)
#
# # 'i' will take all the keys whilst 'j' will take all of the values
# for i, j in my_dictionary.items():
#     print(i, j)
# # Can also iterate through dictionaries
#
# Dictionaries can also be initialized with the 'dict' keyword
cat = dict(name = "Kitty", age = 0.5)


# You can add to a dictionary by utilising square brackets to define key
# and adding corresponding value using = assignment operator
cat["colour"] = "White"
print(cat)

# # Can also pop from a dictionary by declaring a variable and using list.pop(index)
# popped_pair = cat.pop("colour")
# print(popped_pair)

# original_string = "Hello world!"
# new_string = original_string[0:5]
# print(new_string)
#
# stripped_string = original_string.strip()
# print(stripped_string)
#
# sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
# split_sentence = sentence.split("HELLO")
# print(split_sentence)
#
# print("Example 4: ")
# # Replaces dollar sign with 'WOW' in the string
# fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
# fact2 = fact2.replace("$", "WOW!")
#
# print(fact2)
# # Strips leading and trailing whitespace to clean the string
# fact2 = fact2.strip()
# print(fact2)
# # Splits the string into a list of substrings using WOW! as the separator
# fact2 = fact2.split("WOW!")
# print(fact2)
#
# print("Example 5: ")
# string_list = ["I", "like", "to", "join", "lists", "to", "make", "strings"]
# # Initializes a variable to store joint list as a string. " " separates elements in the list with a space
# list_joined = " ".join(string_list)
# print(list_joined)
#

profile_dict = dict(Name = 'Stephen', DOB = '21/03/1984', Age = 21, Height = '5\'11')
profile_dict.update(dict(Weight = '76kg'))

profile_dict['Gender'] = 'Male'

for details in profile_dict:
    print(details)
