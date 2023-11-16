def division(a, b):
    try:
      return a/b
    except: ZeroDivisionError


print(division(1, 0))
print(division(1, 1))
