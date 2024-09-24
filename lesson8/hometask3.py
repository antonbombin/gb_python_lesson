"""
Задача 3. Турнир
В файле first_tour.txt записано число K и данные об участниках турнира по
настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех
участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников
второго тура. Затем программа должна вывести фамилии, инициалы и
количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по
убыванию набранных баллов.
"""

with open("first_tour.txt", "r") as file:
    lines = file.readline()
    K = int(lines[0])
    participants = {}
    filter_player = {}
    count = 1

for line in lines[1:]:
    data = line.strip().split()
    name = f"{data[1][0]}. {data[0]}"
    score = int(data[-1])
    participants[name] = score

for player, score in participants.items():
    if score > K:
        filter_player[player] = score

sorted_filter_player = dict(sorted(filter_player.items(), key=lambda x: x[1], reverse=True))

with open("second_tour.txt", "w") as file:
    file.write(f"{len(sorted_filter_player)}\n")
    for player, score in sorted_filter_player.items():
        file.write(f"{count} {player} {score}\n")
        count += 1
