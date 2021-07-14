# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

numbers = []
with open("files/info.txt", "r") as f:
    for line in f:
        if line.strip().isdigit() or (line.strip()[0]=="-" and line.strip()[1:].isdigit()):
            numbers.append(int(line.strip()))

print(numbers)
print(sum(numbers))
