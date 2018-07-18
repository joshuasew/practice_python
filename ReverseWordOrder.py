# Joshua Sew-Hee
# 6/18/18
# Reverse Word Order

def ReverseWordOrder(input_string):
    words = input_string.split(' ')
    reverse_words = []
    for i in reversed(words):
        reverse_words.append(i)
    result = ' '.join(reverse_words)
    return result

str = input("Enter a string to reverse: ")

print("Original string:")
print(str)
print("Reverse string:")
print(ReverseWordOrder(str))
