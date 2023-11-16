def find_min_number(a, b, c):
    if b <= a and  b <= c: return b
    if c <= b and c <= a: return c
    if a <= b and a <= c: return a

print(find_min_number(1, 2, 3))
