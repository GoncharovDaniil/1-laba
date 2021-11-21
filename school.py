#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    school = {
        '1а': '14 учеников',
        '2б': '16 учеников',
        '3в': '20 учеников'
    }
    print('Изначальный список классов и количество учеников:')
    print(school)

# Организовать бесконечный цикл запроса команд.
while True:
    # Запросить команду из терминала.
    command = input(">>> ").lower()

    if command == 'exit':
       break

    elif command == 'list':
        print('Новый список класса и количество учеников:')
        print(school)

    elif command == '3':

        school = {
            '1а': '14 учеников',
            '2б': '16 учеников',
            '3в': '20 учеников',
            '4г': '13 учеников'
        }
        print('Добавление нового класса:')
        print(school)

    elif command == '2':
        school = {
            '1а': '14 учеников',
            '2б': '16 учеников',
            '4г': '13 учеников'
        }
        print('Удаление класса:')
        print(school)

    elif command == '1':
        school = {
            '1а': '8 учеников',
            '2б': '16 учеников',
            '3в': '20 учеников',
            '4г': '13 учеников'
        }
        print('Изменение количества учеников в одном из классов:')
        print(school)
