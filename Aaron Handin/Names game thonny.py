username = []
userage = []
userband = []
usernum = 1

b = (10) #array tester size

for i in range(b):
    print ("user #", usernum, )
    username.append(input("Enter name: "))
    userage.append(input("Enter age: "))
    userband.append(input("Enter band: "))
    usernum = usernum + 1


for entry in range(b):
    print ("User #", entry + 1, "Details:")
    print  

