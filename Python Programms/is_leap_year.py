def is_leap(year):
    # Вместо pass напишите тело функции
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0)

print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))