# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день


items_sold=[]
items=[]
sold=[]
items_not_repeat=[]
f = open("files/items_sold.txt", "r", encoding="UTF-8")
for line in f:
    items_sold_str=line.replace(":"," ").split()
    for el in items_sold_str:
        items_sold.append(el) # получаю общий список цены и товары
        if el.replace(".","").isdigit():
            sold.append(float(el)) #список цен
        else:
            items.append(el)  #список товаров

print("Общая выручка магазина:", sum(sold))

items_not_repeat=list(set(items))  #список товаров без повтора, для цикла
max_total=0
for item in items_not_repeat:
    k = 0  #переменная 0/1 для перехода на следующий элемент
    total_sold_item = 0  #здесь будет сумма цен на конкретный товар

    for el in items_sold:
        if k==1:
            total_sold_item=total_sold_item+float(el)
            k=0
        if item==el:  #если элементы совпали, то следуюший элемент - нужная мне цена
            k=1       #отмечаю переменную к, чтобы в следующем витке цикла взять цену

    print(f"Сумма оп товару {item}: {total_sold_item}")

    if total_sold_item>max_total:
        max_total=total_sold_item
        max_item=item
print("Наибольшие продажи по товару:",max_item)
print("Количество типов товара:", len(items_not_repeat))

f.close()
