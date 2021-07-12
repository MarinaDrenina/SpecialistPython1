x = 100
a = 7
n = 3
total_simple = x
total_hard = x
for i in range(n):
    total_simple = total_simple + (x * a / 100)
    total_hard = total_hard + (total_hard * a / 100)
if total_hard > total_simple:
    print("Выгоднее сложные проценты")
else:
    print("Выгоднее простые проценты")
