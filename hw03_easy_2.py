# hw 3 easy Лукьянов Максим
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticketList = list(map(int, list(str(ticket_number))))
    print(ticketList)
    if sum(ticketList) / 2 == sum(ticketList[len(ticketList)-3:]):
        return('Ура, билет счастливый!!')
    else:
        return('Повезет в другой раз..')

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))