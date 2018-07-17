# Joshua Sew-Hee
# 6/14/18
# Odd Or Even

number = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide: "))

if (number % 2 == 0):
    print("%d is even." %number)
elif (number % 2 != 0):
    print("%d is odd." %number)

if (number % 4 == 0):
    print("%d is a multiple of 4." % number)

if (number % check == 0):
    print("%d divides evenly in %d" %(number,check))
else:
    print("%d does not divide evenly in %d." %(number,check))
