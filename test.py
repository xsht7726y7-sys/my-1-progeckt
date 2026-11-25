from random import choice
from telebot import TeleBot

TOKEN = '8798139688:AAFARmPgThZXPBmpCpBAmsfHvnCxlRSlHMU'
bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        'Привет! Давай сыграем в «Камень-ножницы-бумага».\n'
        'Напиши: камень, ножницы или бумага.'
    )
def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.message_handler(commands=['duck'])
def duck(message):
    url = random_duck()
    bot.send_message(message.chaid.id, url)







if __name__ == '__main__':
    bot.polling(none_stop=True)