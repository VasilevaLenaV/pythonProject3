# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from functools import reduce


def is_float(c):
    try:
        float(c)
        return True
    except ValueError:
        return False


def is_int(c):
    try:
        int(c)
        return True
    except ValueError:
        return False


digits = lambda y: list(int(a) for a in list(y) if is_int(a))


input_str = input("Задача 1. Введите вещественное число: ")

if is_float(input_str):
    summa = reduce(lambda result, n: result + n, digits(input_str))
    print(f"Сумма -> {summa}")
else:
    print("Введенное значение не является вещественным числом")


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from functools import reduce

get_data = lambda n: list(range(1, n+1))
get_element = lambda k: reduce((lambda x, y: x * y), get_data(k))
get_result = lambda r: list(map(lambda x: get_element(x), get_data(r)))

m = int(input("Задача 2. Введите число: "))
print(get_result(m))


# Задача 3.Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06
from functools import reduce

get_list = lambda n: list(map(lambda a: (1 + 1 / a) ** a, list(range(1, n + 1))))
get_summa = lambda k: reduce((lambda x, y: x + y), k)

input_number = int(input("Задача 3. Введите число: "))
list_numbers = get_list(input_number)
print(list_numbers)
print(f"Сумма {get_summa(list_numbers):.2f}")
