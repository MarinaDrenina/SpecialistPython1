# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_name = ""
max_count = 0
for el in names:
    if len(el) > max_count:
        max_count = len(el)
        max_name = el
print(max_name)
