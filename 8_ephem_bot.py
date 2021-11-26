"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem 

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
} 


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Добрый день!")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_planet(update, context):
    tx = 'Вызван /planet'
    print(tx)
    update.message.reply_text("Какая планета Вам интересна?")

def say_planet(update, context):
  user_ansswer = update.message.text
  print( user_ansswer)
  update.message.reply_text((user_ansswer.split(' , ')))

  planet = ' '
  if planet in user_ansswer:
    planet = ephem.planet.lower()('%s %s' % (j.ra, j.dec)
    constellation = ephem.constellation(planet)
    print(constellation)




  
  
    





  
def main():
    mybot = Updater("2124082861:AAEKRl4wdTqmPJ7MD_2ugocdBHxGVNCuJlk", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text,say_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
  main()
