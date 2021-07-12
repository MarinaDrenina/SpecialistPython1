a = 1
b = 30
total = 0

for i in range(a, b + 1):
    if i > 9 and str(i) == str(i)[::-1]:
        total = total + 1
print(total)...
