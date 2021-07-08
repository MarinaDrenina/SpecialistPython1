# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

first=1,2,3,5
second=5,1,8,7
third=3,5,7,1

num=0
for el in first:
    if second.count(el)>=1 and third.count(el)>=1:
        num=num+1
print(num)
