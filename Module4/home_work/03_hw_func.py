# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dist

def in_round(p1, p2, r1, r2):
    line_round = distance(*p1, *p2)
    return abs(r1 - r2) >= line_round

print(in_round((7, 5), (7, 7), 4, 1))
