#######################################################
# JANREI
# Computer Science 30
# Oct. 3, 2024
#
# Strings
# Purpose: have the user enter a string
# print the string forwards
# print the string backwards
# print the string in all uppercase
# print the string in all lowercase
# count how many spaces are in the string
# count how many vowels are in the string
# count how many consonants are in the string
# count how many other characters are in the string
# count how many numbers are in the string
# display results
# you will need: print, input, let, for-next(step), len, left$, right$, mid$ ucase$, lcase$
# you might need: or, and, (not, xor, xand), if-then-elseif-else-endif, select case
#######################################################

#asks for string
String = input('Enter a string: ')

# count the spaces, vowels, consonants, numbers, and other characters in the string
vowel_count = 0
consonants_count = 0
space_count = 0
numbers_count = 0
other_characters_count = 0

#turns the string upper and lowercase
String_upper = String.upper()
String_lower = String.lower()

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in String: # adds the appropriate amount of characters for each variable
    if char == ' ':
        space_count += 1
    elif char.lower() in vowels:
        vowel_count += 1
    elif char.lower() in consonants:
        consonants_count += 1
    elif char in numbers:
        numbers_count += 1
    else:
        other_characters_count += 1

# print the string in all formats
print(f"String forwards: {String}\n"
      f"String backwards: {String[::-1]}\n"
      f"String in uppercase: {String_upper}\n"
      f"String in lowercase: {String_lower}\n"
      f"Number of vowels: {vowel_count}\n"
      f"Number of spaces: {space_count}\n"
      f"Number of consonants: {consonants_count}\n"
      f"Number of numbers: {numbers_count}\n"
      f"Number of other characters: {other_characters_count}")