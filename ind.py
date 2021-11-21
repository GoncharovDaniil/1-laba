#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    # Список рейсов.
    reis = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о рейсе.
            name = input("Пункт назначения? ")
            number = input("Номер? ")
            tip = input("Тип самолёта? ")

            # Создать словарь.
            samolet = {
                'name': name,
                'number': number,
                'tip': tip,
            }

            # Добавить словарь в список.
            reis.append(samolet)
            # Отсортировать список в случае необходимости.
            if len(reis) > 1:
                reis.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "No",
                    "Пункт назначения",
                    "Номер",
                    "Тип самолёта"
                )
            )
            print(line)

            # Вывести данные о всех рейсах.
            for idx, samolet in enumerate(reis, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        samolet.get('name', ''),
                        samolet.get('number', ''),
                        samolet.get('tip', 0)
                    )
                )

            print(line)

        elif command.startswith('select'):
            # Получить тип самолёта.
            x = input('Введите тип самолёта ')

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения рейсов из списка.
            for samolet in reis:
                if samolet.get('tip') == x:
                    count += 1
                    print('Номер рейса:', samolet.get('number', ''))
                    print('Пункт назначения:', samolet.get('name', ''))

            # Если счетчик равен 0, то рейсы не найдены.
            if count == 0:
                print("Рейсы с заданным типом самолёта не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить данный;")
            print("list - вывести список рейсов;")
            print("select - запросить тип самолёта;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
