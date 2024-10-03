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

#variables to count
vowel_count = 0
consonants_count = 0
space_count = 0
numbers_count = 0

# get user input for a string
String = input("Enter a string: ")

# turn the string to uppercase and lowercase
String_upper = String.upper() # formats the string
String_lower = String.lower()

# count the spaces in the string
for i in range(len(String)):
    if String[i] == ' ':
        space_count += 1

# count the vowels in the string
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(String)):
    if String_lower[i] in vowels:
        vowel_count += 1

# count the consonants in the string
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for i in range(len(String)):
    if String_lower[i] in consonants:
        consonants_count += 1

# count the numbers in the string
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(len(String)):
    if String[i] in numbers:
        numbers_count += 1

# count the other characters in the string
other_characters_count = len(String) - (vowel_count + consonants_count + space_count + numbers_count)

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