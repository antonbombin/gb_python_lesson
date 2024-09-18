"""
Задача 3. Палиндром
Используя модуль collections, реализуйте функцию can_be_poly, которая
принимает на вход строку и проверяет, можно ли получить из неё палиндром.
Пример кода:
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
Результат:
True
False
"""

from collections import Counter

def can_be_poly(val: str) -> bool:

    char_counts = Counter(val)
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))

    return odd_count < 2

print(can_be_poly('eerru'))
print(can_be_poly('abbcba'))
print(can_be_poly('abbbc'))

