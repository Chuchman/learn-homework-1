"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('How old are you? '))

def age_activity(age):
  if age <= 7:
    return ('You should go to kindergarten.')
  elif age >=7 and age < 18:
    return ('You should go to school.')
  elif age >=18 and age < 25:
    return('You should study at college.')
  else:
    return ('You should go for a work!!!') 
#age_res = age_activity(16)
#print(age_res)
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    =)
    """
age_result = age_activity(age)
print(age_result)

if __name__ == "__main__":
    main()
