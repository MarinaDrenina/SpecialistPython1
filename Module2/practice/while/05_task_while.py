# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #

number=int(input("Ввод числа: "))
i=1
while i<=number:
    j = 1
    line = ""
    while j<=number:
        if j==i or j==number-i+1:
            line=line+"#"
        else:
            line = line + " "
        j=j+1
    print(line)
    i=i+1
