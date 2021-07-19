# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найдите любые.
# Является ли данное число(20000-значное) четным?

f=open("files/Big_char.txt","r",encoding="UTF-8")

char_count_list=[]
for i in range(10):
    char_count = 0
    f.seek(0)
    for char in f.readline():
        if int(char)==i:
            char_count=char_count+1
    char_count_list.append(char_count)

print(char_count_list)
print(char_count_list.index(max(char_count_list)))

f.seek(0)
if int(f.readline())%2==0:
    print("Четное число")
else:
    print("Нечетное число")

f.close()
