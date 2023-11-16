def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if int(ticket_str[0])+int(ticket_str[1])+int(ticket_str[2]) == int(ticket_str[3])+int(ticket_str[4])+int(ticket_str[5]) :
        return True
    else:
        return False

print(lucky_ticket(111111))
print(lucky_ticket(123456))
print(lucky_ticket(123321))
