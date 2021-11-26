"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
def hello_user(message):
  while True:
   message = input("How are you doing?")
   if message.lower() == "fine":
     break


    
if __name__ == "__main__":
    hello_user(" How are you doing?")
