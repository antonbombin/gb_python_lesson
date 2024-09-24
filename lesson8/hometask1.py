"""
Задание 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, которые могут быть
разделены пробелами и концами строк. Напишите программу, которая выводит
сумму чисел во выходной файл answer.txt.
"""
import os

numbers_file = open("numbers.txt", "r", encoding="utf-8")

total_sum = 0

for line in numbers_file:
    numbers = [int(num) for num in line.split() if num]
    total_sum += sum(numbers)

numbers_file.close()

sum_file = open("answer.txt", "w", encoding="utf-8")

sum_file.write(str(total_sum))
sum_file.close()
