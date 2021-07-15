# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

import random
def rand_num(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(-20, 20))
    return numbers

lst=rand_num(10)
print(lst)

new_lst=[el for el in lst if el<=10]
print(len(new_lst))

new_lst_pos=[el for el in lst if el>0]
print(sum(new_lst_pos))

new_lst_even=[el for el in lst if el%2==0]
print(sum(new_lst_even)/len(new_lst_even))
