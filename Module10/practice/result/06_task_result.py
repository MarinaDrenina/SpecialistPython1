# Во время проведения олимпиады каждый из участников получил свой идентификационный номер.
# Необходимо отсортировать список участников олимпиады по количеству набранных ими баллов.
# Формат входных данных:
# Для каждого участника олимпиады дается пара чисел: id-участника и количество набранных баллов.
# Формат выходных данных:
# Выведите исходный список в порядке убывания баллов. Если у некоторых участников одинаковые баллы,
# то их между собой нужно упорядочить в порядке возрастания идентификационного номера

olimp=[
    {"id": 1562,
     "score": 100},
    {"id": 12500,
     "score": 500},
    {"id": 3560,
     "score": 50},
    {"id": 15,
     "score": 500},
]
count_id=len(olimp)
new_olimp=[]

for el in range(count_id):
    min_id=min(olimp,key=lambda el:el["id"])
    new_olimp.append(min_id)
    olimp.remove(min_id)

for el in range(count_id):
    max_score=max(new_olimp,key=lambda el:el["score"])
    olimp.append(max_score["id"])
    new_olimp.remove(max_score)
print(olimp)
