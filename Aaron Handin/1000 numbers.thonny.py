######################################################################################################################################
# Aaron Camargo
# Computer science 30
# september 11, 2024
#
#' generate x random numbers from 1-1000 wherein the user defines the amount of numbers generated (x)
#
# store them in an array
# find the average of all the numbers generated
# display the results
#
# how many number you want
# make numbers go into array (make array big enough for numbers to all fit)
# how big are numbers? 1000 is biggest.
# calculate and print the average
######################################################################################################################################

import random

num_of_numbers = int(input("Enter the amount of numbers you want to generate: "))

numbers = []

for i in range(num_of_numbers):
    numbers.append(random.randint(1, 1000000))

sum_of_numbers = sum(numbers)

average = sum_of_numbers / num_of_numbers

print("Here are the numbers generated:", numbers)

print ("here is the average of those numbers:", average)

