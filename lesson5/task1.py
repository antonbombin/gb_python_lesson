"""
Задание 1. Поиск элемента
Пользователь вводит искомый ключ. Если он хочет, то может ввести
максимальную глубину — уровень, до которого будет просматриваться
структура.
Напишите функцию, которая находит заданный пользователем ключ в словаре
и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
качестве примера можно использовать такой словарь:
site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}
"""

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
                }
            }
        }


def find_key(struct, key, max_depth=None, depth=1):
    result = None

    if max_depth and max_depth < depth:
        return result

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, depth = depth + 1)
            if result:
                break

    return result


while True:
    key = input("Введите искомый ключ: ")
    answer = input("Хотите ввести максимальную глубину? Y/N: ")
    if answer.lower() == 'y':
        max_depth = int(input("Введите максимальную глубину: "))
    else:
        max_depth = None

    print('Значение ключа:', find_key(struct=site,max_depth=max_depth, key=key))


