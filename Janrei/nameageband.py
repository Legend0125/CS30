#######################################################
# JANREI
# Computer Science 30
# sept. 10, 2024
#
# Arrays
# Purpose: ask user for their name, age, and favorite band
#loop this 10 times and store the information in 3 arrays.
#display the information back on the screen
#start with this:
####################################################### 

usernum = 1
x = 10
username = []
userage = []
userband = []

for i in range(x):
    username.append(input('What is your name?')) # asks the user to enter a name
    userage.append(input('What is your age?')) # asks the user to enter a age
    userband.append(input('What is your favourite band?')) # asks the user to enter a band

for i in range(x):
    print(f'''user {usernum}. 
    Your name is {username[i]}")
    Your age is {userage[i]}
    Your favorite band is {userband[i]}''')
    usernum += 1