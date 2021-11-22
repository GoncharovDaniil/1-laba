#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    stroki = {
        15: '5+10',
        20: '10+10',
        30: '10+10+10'
    }
    print('Изначальный словарь:')
    print(stroki)

    command = input(">>> ").lower()

    if command == '1':
        stroki.items()
        print('Новый словарь:')
        for key, value in stroki.items():
            print(value, key)
