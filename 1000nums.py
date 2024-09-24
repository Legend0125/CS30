#######################################################
# JANREI
# Computer Science 30
# sept. 10, 2024
#
# generate x random numbers from 1-1000 wherein the user defines the amount of numbers generated (x)
# store them in an array
# find the average of all the numbers generated
# display the results
# you will need: for-next, dim, math, print, let
# how many number you want
# make numbers go into array (make array big enough for numbers to all fit)
# how big are numbers? 1000 is biggest.
# calculate and print the average
#######################################################

import random

numnum = int(input(" how many numbers do you want to generate"))  # how many numbers do you want

numbers = random.choices(range(1, 1001), k=numnum)
total = sum(numbers)
average = total / numnum

print("The numbers you generated are:", numbers)
print("The average is:", average)