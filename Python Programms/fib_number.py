def fib_number(n):
    
    if n == 0:
        return 0
    fib1 = 1
    fib2 = 1
    
    i = 0
    
    while i < n -2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    
    return fib2

print(fib_number(0))
print(fib_number(1))
print(fib_number(2))
print(fib_number(6))
