"""
Задание 2. Сумма чисел
В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
программирования на языке Python. Выглядит он так:
Напишите программу, которая выводит на экран все строки этого файла в
обратном порядке.
"""

philosophical_text = open("zen.txt", "r")

lines = philosophical_text.readline()

philosophical_text.close()

for line in reversed(lines):
    print(line.strip())
