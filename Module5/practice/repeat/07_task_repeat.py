# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.
def deposit(x, a, n):
    total=x
    for i in range(n):
        total=total+(total*a/100)
    return total

print (deposit(100,7,3))
