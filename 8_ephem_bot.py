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
import datetime
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(level=logging.INFO, filename='bot.log')

PROXY = {'proxy_url': settings.PROXY_URL,
'urllib3_proxy_kwargs':{'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет, давай поговорим о космосе?')

def get_planet_consellation(update, context):
    print('Вызвана /planet')
    text = update.message.text
    planet = text.split().title()
    if planet == 'Earth':
        update.message.reply_text('Здорово, мы здесь живем!')
    elif planet in planets:
        planet_today = getattr(ephem, planet)(datetime.datetime.today())
        constellation_today = ephem.constellation(planet_today)
        update.message.reply_text(f'Планета {planet} находится в {constellation_today[1]} сегодня.')
    else: 
        update.message.reply_text('Вы должны выбрать одну из планет солчнечной системы (ввести данные нужно на английском языке)')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', get_planet_consellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Кто-то хочет поговорить с ботом.')

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
