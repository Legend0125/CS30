######################################################################################################################################
# Aaron Camargo
# Computer science 30
# september 11, 2024
#
#' ask user for their name, then their subject, and mark (in any subject)
#' loop this 5 times and store the information in 1 variable and 2 arrays.
#' display the information back on the screen along with their overall average for those 5 classes
######################################################################################################################################
username = input(str("Enter your name: "))

subjects = []

marks = []

classnum = int(input("How many classes do you have?"))

for i in range(classnum):
    subject = input(str("Enter the subject for class " + str(i+1) + ": "))
    subjects.append(subject)
    
    mark = int(input(str("Enter your mark for " + subject + ": ")))
    marks.append(mark)
    
    print("Class " + str(i+1) + " information:")
    print("Subject:", subject)
    print("Mark:", mark)
    print("--------------------")

total_marks = sum(marks)
avergeMarks = total_marks / classnum

print ("Your average between these " , classnum, "classes is: ", avergeMarks)