# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.


def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dist

def min_line (p1, p2, p3):
    AB = distance(*p1, *p2)
    BC = distance(*p2, *p3)
    AC = distance(*p1, *p3)
    if AB<=BC and AB<=AC:
        return "AB"
    elif BC<=AB and BC<=AC:
        return "BC"
    else:
        return "AC"

print("Самый короткий отрезок:", min_line((1, 1), (2, 8), (1, 3)))
