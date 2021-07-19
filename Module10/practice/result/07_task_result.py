# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
import random

f=open("files/Big_char.txt","a",encoding="UTF-8")
for i in range(20000):
    if i==0:
        f.write(str(random.randint(1, 9)))
    else:
        f.write(str(random.randint(0,9)))
