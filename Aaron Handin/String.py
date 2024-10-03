
######################################################################################################################################
# Aaron Camargo
# Computer science 30
# October 3, 2024
#'have the user enter a string
#'print the string forwards
#'print the string backwards
#'print the string in all uppercase
#'print the string in all lowercase
#'count how many spaces are in the string
#'count how many vowels are in the string
#'count how many consonants are in the string
#'count how many other characters are in the string
#'count how many numbers are in the string
#'display results
######################################################################################################################################

user_input = input("Enter a string: ") # input string

print("String forwards:", user_input) # output string

print("String backwards:", user_input[::-1]) # output string backwards

print("String in uppercase:", user_input.upper()) # output string in all uppercase characters

print("String in lowercase:", user_input.lower()) # output string in all lowercase characters

# variables for counting the number of different characters

space_count = 0 

vowel_count = 0 

consonant_count = 0

other_char_count = 0

number_count = 0

for char in user_input: #Adds to the counter variable
    if char.isspace():
        space_count += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        number_count += 1
    else:
        other_char_count += 1

# Prints results

print("Number of spaces:", space_count)

print("Number of vowels:", vowel_count)

print("Number of consonants:", consonant_count)

print("number of other characters:", other_char_count)

print("Number of numbers:", number_count)

print("All done!")
