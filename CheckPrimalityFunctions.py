# Joshua Sew-Hee
# 6/15/18
# Check Primality Functions

number = int(input("Enter a number to check if it is prime: "))

x = list(range(1,number+1))
# print(x)
factors = []
for elem in x:
    if(number % elem == 0):
        factors.append(elem)
print("Factors of {}:".format(number))
print(factors)
if(len(factors) == 2):
    print("{} is prime".format(number))
else:
    print("{} is not prime".format(number))
