#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_f(name, surname, yearbirth, email, telefon,):
    print(name, surname,  yearbirth, email, telefon)
my_f(surname='Pavel', name='Simakin', yearbirth = 2020, email = '123@mail.net' , telefon = 123456789)
# my_f('Ivan', surname='ivanoc', age=20)