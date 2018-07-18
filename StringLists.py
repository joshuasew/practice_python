# Joshua Sew-Hee
# 6/14/18
# String Lists: Palindrome

import math
# this function removes all symbols and spaces from a string replacing
# them by "no space"
def strip_all(string1):
    syms = " ,.!:;()-_?\'\""
    for sym in syms:
        string1  = string1.replace(sym, '')
    return string1

print("This program checks whether this string is a palindrome.")
user_string = input("Enter a string: ")
# convert the string to lowercase to equal comparison
a = user_string.lower()
a = strip_all(a)
# print(a)
count = 0
for i in range(math.floor(len(a)/2)):
    if (a[i] == a[len(a) - 1 -i]):
        #print(a[i])
        count = count + 1

if count == math.floor(len(a)/2):
    print("\"%s\" is a palindrome." %user_string)
else:
    print("\"%s\" is not a palindrome." %user_string)
