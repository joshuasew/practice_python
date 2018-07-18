# Joshua Sew-Hee
# 6/15/18
# Fibonacci

def Fibonacci(limit):
    old_fib = 0
    current_fib = 1
    new_fib = 0
    print("{}, {}, ".format(old_fib,current_fib), end='')
    for i in range(2,limit):
        new_fib = old_fib + current_fib
        print(new_fib, end='')
        if i != (limit-1):
            print(", ", end='')
            # far left becomes the current fib first
            old_fib = current_fib
            # the middle becomes the new fib
            current_fib = new_fib
        else:
            print(", ...")


def n_Fibonacci(n):
    old_fib = 0
    current_fib = 1
    new_fib = 0
    for i in range(2,n):
        new_fib = old_fib + current_fib
        old_fib = current_fib
        current_fib = new_fib
    print(new_fib)


limit = int(input("How many Fibonacci numbers do you want to generate? "))
Fibonacci(limit)
n = int(input("Which nth Fibonacci number do you want? "))
n_Fibonacci(n)
