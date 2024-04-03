# Create functions to store calculation of alternating case and word.
# .join creates one single string.
# if statement needed in conjunction with modulus to keep track of odd/even iterations.
# string methods of .lower and .upper modify char/words to lower or upper case.
# example_string stores a string variable to showcase functionality.
# Print both examples.

def alternate_case_conversion(a_string):
    result = ''.join([char.upper() if i % 2 == 0
                      else char.lower() for i, char in enumerate(a_string)])
    return result


example_string = "This has been a very informative task."
print(alternate_case_conversion(example_string))


def alternative_word_conversion(a_string):
    # Variable 'words' splits a_string into words
    words = a_string.split()
    # ' '.join ensure the sentence has a space and enumerate yields index and value
    result = ' '.join([word.lower() if i % 2 == 0
                       else word.upper() for i, word in enumerate(words)])
    return result


print(alternative_word_conversion(example_string))
