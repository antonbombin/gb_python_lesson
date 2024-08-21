"""
Задача 5. Пицца
В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и
сколько заказывал у них в определённый период. Вам нужно структурировать
эту информацию и определить, сколько всего пицц купил каждый заказчик.
На вход в программу подаётся N заказов. Каждый заказ представляет собой
строку вида «Покупатель — название пиццы — количество заказанных пицц».
Реализуйте код, который выводит список покупателей и их заказов по
алфавиту. Учитывайте, что один человек может заказать одну и ту же пиццу
несколько раз.

Пример
Введите количество заказов: 6
Первый заказ: Иванов Пепперони 1
Второй заказ: Петров Де-Люкс 2
Третий заказ: Иванов Мясная 3
Четвёртый заказ: Иванов Мексиканская 2
Пятый заказ: Иванов Пепперони 2
Шестой заказ: Петров Интересная 5
Иванов:
Мексиканская: 2
Мясная: 3
Пепперони: 3
Петров:
Де-Люкс: 2
Интересная: 5
"""

order = int(input("Введите количество заказов: "))
database = dict()

for i_order in range(order):
    customer, pizza_name, count = input('{} заказ: '.format(i_order + 1)).split()

    count = int(count)

    if customer not in database:
        database[customer] = {pizza_name: count}

    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name] += count

        else:
            database[customer][pizza_name] = count


for customer in sorted(database.keys()):
    print('{}: '.format(customer))
    for pizza_name in sorted(database[customer].keys()):
        print('    {}: {}'.format(pizza_name, database[customer][pizza_name]))




