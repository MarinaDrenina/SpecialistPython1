# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

a = int(input("Сторона квадрата: "))
i = 2
line_up = "#"
while i <= a:
    line_up = line_up + "#"
    i = i + 1
print(line_up)
i = 2
line_in = "#"
while i < a:
    line_in = line_in + " "
    i = i + 1
line_in = line_in + "#"
i = 2
while i < a:
    print(line_in)
    i = i + 1
print(line_up)
