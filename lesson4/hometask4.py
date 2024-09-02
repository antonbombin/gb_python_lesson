"""
Задача 4. Гистограмма частоты
Создайте программу для лингвистов, которая будет инвертировать полученный
словарь. То есть в качестве ключа будет частота, а в качестве значения —
список символов с этой частотой. Вам нужно реаллизовать:
1. получить текст и создать из него оригинальный словарь частот;
2. создать новый словарь и заполнить его данными из оригинального
словаря частот, используя количество повторов в качестве ключей, а
буквы — в качестве значений, добавляя их в список для хранения.
"""


def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


text = input("Введите текст: " )

hist = histogram(text)

print("Оригинальный словарь частот: ")
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

inv_hist = invert_dict(hist)

print('\nИнвертированный словарь частот: ')
for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ":", inv_hist[i_sym])
