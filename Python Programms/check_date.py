def check_date(day, month, year):
    def is_leap(year):
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        return False
    
    if type(day) is not int:
        return False  
    if type(month) is not int:
        return False
    if type(year) is not int:
        return False
    
    if month > 12 or month < 1:
        return False
    if 1 > day > 31:
        return False
        
    if month in [2, 4, 6, 9, 11] and day > 30:
        return False
        
    if year < 1900:
        return False
    if year > 2022:
        return False 
        
    if month == 2:
        if is_leap(year):
            if day > 29:
                return False
        elif day > 28:
            return False
    return True

print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))