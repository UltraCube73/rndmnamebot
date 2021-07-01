import telebot
import random
bot = telebot.TeleBot('1800538540:AAGH1UY9jg5nAA1gh42oHANItQbyHbNCF98');
firstnames = ['Artur', 'Igor`', 'Pavel', 'Egor', 'Nikita', 'Adolf']
lastnames = ['Kuznetsov', 'Ivanov', 'Vasil`ev', 'Petrov', 'Sokolov']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help' or message.text == '/start':
        bot.send_message(message.from_user.id, 'Введите /name для получения случайного имени или /num для получения числа от 0 до 100')
    elif message.text == '/name':
        fnamenumber = random.randint(0, len(firstnames) - 1)
        lnamenumber = random.randint(0, len(lastnames) - 1)
        bot.send_message(message.from_user.id, firstnames[fnamenumber] + ' ' + lastnames[lnamenumber])
    elif message.text == '/num':
        bot.send_message(message.from_user.id, random.randint(0, 100))
    else:
        bot.send_message(message.from_user.id, 'Неверная команда. Введите /help для просмотра списка команд.')

bot.polling(none_stop=True, interval=0)