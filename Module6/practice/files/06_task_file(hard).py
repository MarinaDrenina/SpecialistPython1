# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

f_hours = open("files/hours_of.txt", "r", encoding="UTF-8")
f_workers = open("files/workers.txt", "r", encoding="UTF-8")
f_workers_hours= open("files/workers_hours.txt", "a", encoding="UTF-8") #создаю файл для объединения

line_w_count=[]  #собираю длины строк в workers, чтобы взять максимальную
for line_w in f_workers:
    line_w_count.append(len(line_w))

f_workers.seek(0)
for line_w in f_workers:
    f_hours.seek(0)
    for line_h in f_hours:
        if line_w.split()[0]==line_h.split()[0] and line_w.split()[1]==line_h.split()[1]: #если имя и фамилия равны
            count_space=max(line_w_count)-len(line_w.rstrip())+4  #считаю сколько нужно добавить пробелов
            #новая таблица с данными из двух:
            f_workers_hours.write(line_w.rstrip()+" "*count_space+line_h.strip().split()[2]+"\n")
f_hours.close()
f_workers.close()
f_workers_hours.close()

len_line=0
f_workers_hours= open("files/workers_hours.txt", "r", encoding="UTF-8")
f_result= open("files/result.txt", "a", encoding="UTF-8") #итоговый файл в нем будет предыдущий +зп
for line in f_workers_hours:
    if line.split()[0]=="Имя":
        f_result.write(line.rstrip() + " " * 4 + "Зарплата на руки" + "\n")
        len_line=len(line.rstrip())
    else:
        if int(line.split()[4])>int(line.split()[5]):
            salary=int(line.split()[5])*int(line.split()[2])/int(line.split()[4])
        else:
            salary=int(line.split()[2])+2*(int(line.split()[5])-int(line.split()[4]))*int(line.split()[2])/int(line.split()[4])
        print(salary)
        count_space = len_line - len(line.rstrip()) + 4
        f_result.write(line.rstrip() + " " * count_space  + str(round(salary,2)) + "\n")
f_workers_hours.close()
f_result.close()
