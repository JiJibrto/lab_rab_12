# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
# должен включать в себя не менее четырех функций инициализации: числами, строкой
# (например, «23:59:59»), секундами и временем.
# Обязательными операциями являются:
# вычисление разницы между двумя моментами времени в секундах, ----
# сложение времени и заданного количества секунд,
# вычитание из времени заданного количества секунд,
# сравнение моментов времени, ----
# перевод в секунды,
# перевод в минуты (с округлением до целой минуты).
import time


class Time:

    def __init__(self):
        self.__time1 = []

    @staticmethod
    def __interpreter(__s):
        __sec = __s
        __min = __sec // 60
        __hou = __min // 60
        __min = __min % 60
        __sec = __sec % 60
        __time = [__hou, __min, __sec]
        return __time

    def reverse_interpreter_sec(self):
        __sec = self.__time1[0] * 3600 + self.__time1[1] * 60 + self.__time1[2]
        return __sec

    def reverse_interpreter_min(self):
        __min = self.__time1[0] * 60 + self.__time1[1] + (0 if self.__time1[2] == 0 else 1)
        return __min

    def read_time_num(self):
        self.__time1 = []
        self.__time1.append(int(input("Set hours> ")))
        self.__time1.append(int(input("Set minutes> ")))
        self.__time1.append(int(input("Set seconds> ")))
        self.__time1 = self.__interpreter(self.reverse_interpreter_sec())

    def read_time_str(self):
        self.__time1 = []
        self.__time1 = list(map(int, input("Set time (*:*:*)> ").split(":", maxsplit=2)))
        self.__time1 = self.__interpreter(self.reverse_interpreter_sec())

    def read_time_sec(self):
        self.__time1 = []
        self.__time1 = self.__interpreter(int(input("Set seconds> ")))

    def read_time_now(self):
        self.__time1 = []
        self.__time1 = self.__interpreter(int(time.time()))

    def display(self):
        print(f"{self.__time1}")

    def sum_sec(self, __s):
        return self.reverse_interpreter_sec() + __s

    def dif_sec(self, __s):
        return self.reverse_interpreter_sec() - __s


if __name__ == '__main__':
    new_time1 = Time()
    new_time2 = Time()
    print("Варианты инициализации: \n\nСтрокой: ")
    new_time1.read_time_str()
    new_time1.display()
    print("\nПо настоящему времени: ")
    new_time1.read_time_now()
    new_time1.display()
    print("\nСекундами: ")
    new_time1.read_time_sec()
    new_time1.display()
    print("\nЦифрами: ")
    new_time1.read_time_num()
    new_time1.display()

    print(f"\nСложение времени и заданного количества секунд: {new_time1.sum_sec(int(input('Enter seconds> ')))}")
    print(f"\nВычитание из времени заданного количества секунд: {new_time1.dif_sec(int(input('Enter seconds> ')))}")
    print(f"\nПеревод в секунды: {new_time1.reverse_interpreter_sec()}")
    print(f"Перевод в минуты (с округлением до целой минуты): {new_time1.reverse_interpreter_min()}")

    print("\nИнициализация второго обьекта времени")
    new_time2.read_time_num()
    new_time2.display()

    print(f"\nВычисление разницы между двумя моментами времени в секундах: {new_time1.reverse_interpreter_sec() - new_time2.reverse_interpreter_sec()}")
    if new_time1.reverse_interpreter_sec() > new_time2.reverse_interpreter_sec():
        print(f"Сравнение моментов времени: new_time1 > new_time2")
    elif new_time1.reverse_interpreter_sec() < new_time2.reverse_interpreter_sec():
        print(f"Сравнение моментов времени: new_time1 < new_time2")
    else:
        print(f"Сравнение моментов времени: new_time1 == new_time2")
