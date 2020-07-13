# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
# import random
# random.seed(6)
# print(random.random())
# print(random.randint(0, 10))
# print(random.randrange(0, 10, 3)


from functools import reduce


def mul_list(n1, n2):
    return n1 * n2


my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(mul_list, my_list))