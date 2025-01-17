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
def get_line(line_1, line_2):
  if  not type(line_1) == str or not type(line_2) == str:
    return 0

  if line_1 == line_2:
    return 1
  elif line_1 != line_2 and  len(line_1) > len(line_2):
    return 2
  elif line_1 != line_2 and line_2 == 'learn':
    return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    answer = get_line( 'lnt','learn')
    print(answer)
    
if __name__ == "__main__":
    main()
