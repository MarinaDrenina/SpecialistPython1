# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random

import random
def rand(n,a=0,b=9):
    my_list=[]
    for i in range(n):
        my_list.append(random.randint(a,b))
    return(my_list)

print(rand(5))
