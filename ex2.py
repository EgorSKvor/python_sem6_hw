# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
num = int(input('--> '))


def do_it(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        while (num % i == 0):
            print(i)
            num //= i


do_it(num)
if num != 1:
    print(num)
