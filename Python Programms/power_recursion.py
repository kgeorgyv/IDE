def power(val, n):
    if n != 1:
        return power(val,n-1)*val
    else:
        return val

print(power(2,3))