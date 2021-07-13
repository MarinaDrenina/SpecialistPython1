# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)

path = "files/salaries.txt"
f = open(path, "r", encoding="UTF-8")
f_new=open("files/highly_paid.txt", "w", encoding="UTF-8")
for line in f:
    new_line=line.split()
    if new_line[3]!="Зарплата":
        if int(new_line[3])>60000:
            print(new_line)
            f_new.write(new_line[0])
            f_new.write(" ")
            f_new.write(new_line[0][0])
            f_new.write(" ")
            f_new.write(new_line[1][0])
            f_new.write("\n")
