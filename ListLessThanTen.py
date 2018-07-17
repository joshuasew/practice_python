# Joshua Sew-Hee
# 6/14/18
# List Less Than Ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Numbers less than 5: ")
for i in range(len(a)):
    # check if element is less than 5 and print it
    if (a[i] < 5):
        print(a[i])

# extras 1, 2
# create an empty list to hold the elements that are less than 5
b = []
print("List of numbers less than 5: ")
for j in a:
    if(j < 5):
        b.append(j)
print(b)

# extras 3
# create an empty list to hold the elements that are less than the number
# entered by the user
c = []
number = int(input("Enter a number: "))
print("List of numbers less than {}: ".format(number))
for k in a:
    if(k < number):
        c.append(k)
print(c)
