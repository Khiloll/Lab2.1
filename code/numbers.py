
# Запросите у пользователя четыре числа 
# (файл numbers.py). Отдельно сложите первые 
# два и отдельно вторые два. Разделите 
# первую сумму на вторую. Выведите результат 
# на экран так, чтобы ответ содержал две цифры 
# после запятой.

x_1 = float(input('Enter the first number: '))
x_2 = float(input('Enter the second number: '))
x_3 = float(input('Enter the third number: '))
x_4 = float(input('Enter the fourth number: '))

summa_1 = x_1 + x_2
summa_2 = x_3 + x_4

result = round(summa_1 / summa_2, 2)

print(result)
