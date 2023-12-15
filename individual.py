def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

def quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4):
    area1 = triangle_area(x1, y1, x2, y2, x3, y3)
    area2 = triangle_area(x1, y1, x3, y3, x4, y4)
    total_area = area1 + area2
    return total_area

# Получаем координаты вершин четырехугольника от пользователя
x1, y1 = map(int, input("Введите координаты x1 y1 через пробел: ").split())
x2, y2 = map(int, input("Введите координаты x2 y2 через пробел: ").split())
x3, y3 = map(int, input("Введите координаты x3 y3 через пробел: ").split())
x4, y4 = map(int, input("Введите координаты x4 y4 через пробел: ").split())

# Вычисляем площадь и выводим результат
result = quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4)
print("Площадь четырехугольника:", result)
