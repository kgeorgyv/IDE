def find_min_number(a, b, c):
    if b <= a and  b <= c: return b
    if c <= b and c <= a: return c
    if a <= b and a <= c: return a

def find_middle_number(a, b, c):
    if (b >= a and  b <= c) or (b <= a and  b >= c): return b
    if (c >= b and c <= a) or (c <= b and c >= a) : return c
    if (a >= b and a <= c) or (a <= b and a >= c)  : return a


def sum_min_numbers(a, b, c):
  return find_min_number(a, b, c) + find_middle_number(a, b, c)

print(sum_min_numbers(-2, -1, -3))
 

