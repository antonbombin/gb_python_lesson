"""
Задача 4. Частотный анализ
Есть файл text.txt, который содержит текст. Напишите программу, которая
выполняет частотный анализ, определяя долю каждой буквы английского
алфавита в общем количестве английских букв в тексте, и выводит результат в
файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
тремя знаками в дробной части. Буквы должны быть отсортированы по
убыванию их доли. Буквы с равной долей должны следовать в алфавитном
порядке.
"""

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_letters = 0
with open("text.txt", "r") as file:
    text = file.read().lower()

letter_count = {letter: 0 for letter in english_alphabet}
for char in text:
    if char in english_alphabet:
        letter_count[char] += 1
        total_letters += 1

letter_freq = {letter: (count / total_letters) for letter, count in letter_count.items() if count > 0}

sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

with open("analysis.txt", "w") as file:
    for letter, freq in sorted_letters:
        file.write(f"{letter} {freq:.3f}\n")
