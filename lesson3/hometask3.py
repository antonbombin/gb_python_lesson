"""
Задача 3. Сортировка
Дан список из N чисел. Напишите программу, которая сортирует элементы
списка по возрастанию и выводит их на экран. Дополнительный список
использовать нельзя.
Также нельзя использовать готовые функции sorted/min/max и метод sort
Постарайтесь придумать и написать как можно более эффективный алгоритм
сортировки.
Пример:
Изначальный список: [1, 4, –3, 0, 10]
Отсортированный список: [–3, 0, 1, 4, 10]
"""

my_list = [1, 4, -3, 0, 10]

print('Изначальный список: ', my_list)

for i in range(len(my_list) - 1):
    for j in range(len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print('Отсортированный список', my_list)

