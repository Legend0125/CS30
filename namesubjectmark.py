#######################################################
# JANREI
# Computer Science 30
# Sept. 11, 2024
#
# Arrays2
# ask user for their name, then their subject, and mark (in any subject)
# loop this 5 times and store the information in 1 variable and 2 arrays.
# display the information back on the screen along with their overall average for those 5 classes
####################################################### 

name = input("Enter your name: ")
classes = int(input("Enter the number of classes you have: "))
subjects = []
marks = []
total_marks = 0

for i in range(classes):
    subject = input("Enter subject {}: ".format(i+1))
    subjects.append(subject)
    
    indmark = int(input("Enter mark for {}: ".format(subject)))
    marks.append(indmark)
    total_marks += indmark

average_mark = total_marks / 5

print("Student Name: " + name)
for subject in subjects:
    mark = marks[subjects.index(subject)]
    print("Subject: " + subject + ", Mark: " + str(mark))
print("Overall Average Mark: " + str(average_mark))