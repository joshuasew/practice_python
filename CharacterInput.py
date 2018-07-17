# Joshua Sew-Hee
# 6/14/18
# Character Input

name = input("Enter your name: ")
age = input("Enter your age: ")
copies = input("Enter number of copies: ")

for i in range(int(copies)):
    print("You will turn 100 years old in %d years." %(100 - int(age)))
