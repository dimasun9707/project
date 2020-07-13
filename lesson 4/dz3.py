# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

for i in range(20, 241, ):
    quotient = (i / 20)
    if i % 20 == 0:
        print(f"{i} делится на 20, результат {int(quotient)}.")


# that_list = list(range(20,240))
# x = 89
# if x in that_list:
#     print('cool')
#
#
# my__list = list(range(20,240))
# print (list(map(({i / 20} for el in {int(quotient)} if i % 20 == 0))))
# print(new_list)
# for i in new_list:
#     print(i)

# def numbers(m, count):
#     for i in range(20,240,20):
#         print(numbers())
#      print(i)
# print(range(n for n in range(20, 240) if n % 20 == 0]))
# multiples_5 = [n for n in range(20, 240) if n % 20 == 0]
# multiples_5
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
#
# import random
# /print(randrange(20, 240, 20))

