"""
Задача 2. Zip
Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N
элементов. Создайте кортежи из пар элементов списков и запишите их в список
results. Не используйте функцию zip. Решите задачу в одну строку (не считая
print(results)).
"""

from typing import List, Tuple

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), strings, numbers))

print(results)
