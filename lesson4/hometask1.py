"""
Задание 1. Три списка
Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
Нужно выполнить две задачи:
1. найти элементы, которые есть в каждом списке;
2. найти элементы из первого списка, которых нет во втором и третьем
списках.
Каждую задачу нужно выполнить двумя способами:
1. без использования множеств;
2. с использованием множеств.
"""

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_4 = array_1 + array_2 + array_3

new_elem_1 = []

for i in array_4:
    if i not in new_elem_1 and all(i in array for array in [array_1, array_2, array_3]):
        new_elem_1.append(i)
print("Решение без множеств: ", new_elem_1)

new_elem_1_set = set(array_1) & set(array_2) & set(array_3)
print("Решение с множествами: ", new_elem_1_set)


new_elem_2 = []

for i in array_1:
    if i not in array_2 and i not in array_3:
        new_elem_2.append(i)
print("Решение без множеств: ", new_elem_2)

new_elem_2_set = set(array_1) - set(array_2) - set(array_3)
print("Решение с множествами: ", new_elem_2_set)




