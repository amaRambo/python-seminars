import telebot
from telebot import types
import datetime
bot = telebot.TeleBot("5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"/button")
    
@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Сделать предложение")
    but2 = types.KeyboardButton("узнать время")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)


@bot.message_handler(content_types = "text")
def controller(message):
    print(message.text)
    if message.text == "Сделать предложение":
        bot.send_message(message.chat.id,"введи имя фамилию")
        bot.register_next_step_handler(message,sentence)
    elif message.text == "узнать время":
        bot.send_message(message.chat.id,f"текущее время - {datetime.datetime.now()}")
        button(message)
        
def sentence(message):
    text = message.text
    surname = text.split()[0]
    name = text.split()[1]
    bot.send_message(message.chat.id,f"Вас зовут - {name}, фамилия - {surname}")
    button(message)
    
bot.infinity_polling()






# import telebot
# from telebot import types

# bot = telebot.TeleBot('5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4')

# @bot.message_handler(commands = ['start'])
# def start(message):
#     bot.send.message(message.chat.id, 'напиши клавиатура')

# @bot.message_handler(commands = ['text'])
# def button(message):
#     if message.text == 'клавиатура':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         but1 = types.KeyboardButton('сделать предложение')
#         but2 = types.KeyboardButton('какое время?')
#         markup.add(but1)
#         markup.add(but2)
#         bot.send.message(message.chat.id, 'выбери ниже', reply_markup = markup)
        

# def start(message):
#     bot.send_message(message.chat.id, 'напиши фамилию и имя на одной строчке')
#     bot.register_next_step_handler(message, sentence)
# def sentence(message):
#     text = message.text
#     surname = text.split()[0]
#     name = text.split()[1]
#     bot.send.message(message.chat.id, f'вас зовут {name} {surname}' )
