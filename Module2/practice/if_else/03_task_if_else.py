# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

a=int(input("1 сторона треугольника: "))
b=int(input("2 сторона треугольника: "))
c=int(input("3 сторона треугольника: "))

if a==b or b==c or c==a:
    print ("YES")
else:
    print("NO")
