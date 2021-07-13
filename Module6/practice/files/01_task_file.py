# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "files/limericks.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в тойже папке что и текущий файл

# Открываем файл на чтение
f = open(path, "r", encoding="UTF-8")
# В переменную line считываем строку за стройкой из файла(f)
len_line=0
count_line=0
for line in f:
    print (line.rstrip())
    len_line=len_line+(len(line)-len(line.strip()))
    if line=="\n":
        count_line=count_line+1
print(len_line)
print(count_line+1)

f.close()
# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.
