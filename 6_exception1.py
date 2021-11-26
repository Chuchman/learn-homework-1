"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def hello_user(message):
  try:
    while True:
      message = input("How are you doing?")
      if message.lower() == "fine":
        break
  except KeyboardInterrupt:
    print("пока!")
        


    



    
    
if __name__ == "__main__":
    hello_user("How are you doing?")
