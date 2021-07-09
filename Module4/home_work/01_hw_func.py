# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    # Первое решение через строки
    # t_num = str(ticket_number)
    # if len(t_num) == 6:
    #     for i in range(3):
    #         sum1 = sum1 + int(t_num[i])
    #         sum2 = sum2 + int(t_num[i + 3])
    # return sum1 == sum2 and len(t_num) == 6

    # Второе решение через числа
    copy_t_num1 = ticket_number // 1000
    copy_t_num2 = ticket_number % 1000
    if 100000 <= ticket_number < 1000000:
        for i in range(1, 4):
            sum1 = sum1 + copy_t_num1 % 10
            sum2 = sum2 + copy_t_num2 % 10
            copy_t_num1 = copy_t_num1 // 10
            copy_t_num2 = copy_t_num2 // 10
    return sum1 == sum2 and 100000 <= ticket_number < 1000000

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
