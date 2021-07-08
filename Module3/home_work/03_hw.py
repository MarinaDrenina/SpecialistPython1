# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

n = 10
total = 0
numbers = []

for i in range(n):
    numbers.append(random.randint(-100, 100))
    if numbers[i] % 2 == 0 and numbers[i] > 0:
        total = total + numbers[i]
print(numbers)
print(total)
