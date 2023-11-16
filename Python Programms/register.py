def register(surname, name, date, middle_name = None, registry = list()):
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

    if not check_date(date[0],date[1],date[2]):
        raise ValueError('Invalid Date!')
    else:
        registry.append((surname,name,middle_name,date[0],date[1],date[2]))
        
    return registry
    
reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)
# [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]
 
reg = register('Ivanov', 'Sergej', (24, 13, 1995))
# ValueError: Invalid Date!