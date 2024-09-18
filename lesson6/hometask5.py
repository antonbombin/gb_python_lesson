"""
Задача 5. Шифр Цезаря
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
заменялась на следующую по алфавиту через K позиций по кругу. Если взять
русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение и значение сдвига. Напишите программу,
которая изменит фразу при помощи шифра Цезаря.
"""

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)]
             if sym in alphabet else sym)
             for sym in string]

    new_str = ''.join(char_list)
    return new_str


input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)

print('Зашифрованное сообщение: ', output_str)

