# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def my_score(s):
    numbers=s.split(" ")
    num1=numbers[0]
    if num1.find("/")>0:
        chis1=int(num1[0:len(num1)-2])
        znam1=int(num1[len(num1)-1])
    else:
        chis1=int(num1)
        znam1=1
    num2=numbers[2]
    if num2.find("/")>0:
        chis2 = int(num2[0:len(num2) - 2])
        znam2 = int(num2[len(num2) - 1])
    else:
        chis2 = int(num2)
        znam2 = 1

    if numbers[1]=="+":
        new_num_chis=chis1*znam2+chis2*znam1
    else:
        new_num_chis = chis1 * znam2 - chis2 * znam1
    new_num_znam=znam1*znam2

    if new_num_znam>new_num_chis:
        itog=str(new_num_chis)+"/"+str(new_num_znam)
    elif new_num_znam==1:
        itog = str(int((new_num_chis / new_num_znam) // 1))
    else:
        itog=str(int((new_num_chis/new_num_znam)//1)) +" "+str(new_num_chis%new_num_znam)+"/"+str(new_num_znam)

    return(itog)

print (my_score("5/6 + 4/7"))
print (my_score("-2/3 - -2"))


