# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

f = open("files/fruits.txt", "r", encoding="UTF-8")
for line in f:
    if line != "\n":
        f_new = open("files/fruits/fruits_" + line[0] + ".txt", "a", encoding="UTF-8")
        f_new.write(line)
        f_new.close()
f.close()
