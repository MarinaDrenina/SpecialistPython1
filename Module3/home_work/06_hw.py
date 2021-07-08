# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

list_brand=[]
list_brand_unik=[]
brands=""
for i in range(len(items)):
    list_brand.append (items[i]["brand"])
list_brand_unik=set(list_brand)

for i,el in enumerate(list_brand_unik,1):
    brands=brands+el
    if i<len(list_brand_unik):
        brands = brands+", "
print(brands)

print("На складе больше всего товаров брэнда(ов): ")

max_count=0
many=""
for el in list_brand_unik:
    if list_brand.count(el)>max_count:
        max_count=list_brand.count(el)
        many=el
    elif list_brand.count(el)==max_count:
        many=many+", "+el
print(many)

print("На складе самый дорогой товар брэнда(ов): ")
max_price=0
rich=""
for i in range(len(items)):
    if items[i]["price"]>max_price:
        max_price=items[i]["price"]
        rich=items[i]["brand"]
print(rich)
