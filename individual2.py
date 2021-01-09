# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# сложения и деления. Создать производный класс Real, в котором реализовать метод
# возведения в произвольную степень, и метод для вычисления логарифма числа.

import math


class Number:
    def __init__(self, num):
        self.a = float(num)

    def sum(self, b):
        return self.a + b

    def deg(self, b):
        return self.a / b


class Real (Number):
    def expo(self, b):
        return self.a ** b

    def log(self, b):
        return math.log(self.a, b)


if __name__ == '__main__':
    print("Инициализация обьекта класса Number")
    a = Number(input("Enter a> "))
    print(f"Сумма чисел: {a.sum(float(input('Enter b> ')))}")
    print(f"Деление чисел: {a.deg(float(input('Enter b> ')))}")

    print("Инициализация обьекта класса Real")
    b = Real(input("Enter a> "))
    print(f"Нахождение логарифма: {b.log(int(input('Enter b> ')))}")
    print(f"Возведение в степень: {b.expo(int(input('Enter b> ')))}")
