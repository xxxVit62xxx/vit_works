"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str_1, str_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """


    if type(str_1) != str:
        return 0

    elif str_1 == str_2:
        return 1

    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2

    elif str_1 != str_2 and str_2 == "learn":
        return 3

    else:
        return None
        
str_1 = input('Введите строку №1: ')
str_2 = input('Введите строку №2: ')
print(main(str_1, str_2))

    
if __name__ == "__main__":
    main(str_1, str_2)
