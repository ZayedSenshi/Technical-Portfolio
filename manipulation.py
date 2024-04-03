#Ask user to enter a sentence using input() function. Save variable called str_manip
#calculate and display the length of str_manip
#Find the last letter in str_manip sentence. Replace every occorunce of this letter in str_manip with @
#print the last three characters in str_manip backwards
#create a five letter word that is made up of the first three characters and the last two characters in str_manip
str_manip = input("Please enter a sentence: ")
print(len(str_manip))
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, '@')
print(str_manip[-3:][::-1])
five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)