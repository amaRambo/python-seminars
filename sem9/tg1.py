import telebot
from telebot import types
import random
from random import randint
bot = telebot.TeleBot("5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4")



sweets = 80
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id,f"Приветствую вас в игре!")
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    flag = random.choice(["user", "bot"])
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")
        controller(message)
    else:
        bot.send_message(message.chat.id, f"Первым ходит бот")
        controller(message)
        
def controller(message):
    global flag
    if sweets>0:
        if flag == "user":
            mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            key1 = telebot.types.KeyboardButton("21")
            key2 = telebot.types.KeyboardButton("15")
            mrk.add(key1)
            mrk.add(key2)
            bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet}",reply_markup=mrk)
            bot.register_next_step_handler(message,user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")

def bot_input(message):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global flag,user_turn,sweets
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()


# @bot.message_handler(commands = ["start"])
# def start(message):
#     bot.send_message(message.chat.id,"/button")
    
# @bot.message_handler(commands = ["button"])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     but1 = types.KeyboardButton("узнать правила игры")
#     but2 = types.KeyboardButton("играть")
#     markup.add(but1)
#     markup.add(but2)
#     bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

# @bot.message_handler(content_types = "text")
# def controller(message):
#     print(message.text)
#     if message.text == "узнать правила игры":
#         bot.send_message(
#             message.chat.id,
#             "На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга."
#             "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет." 
#             "Все конфеты оппонента достаются сделавшему последний ход."
#         )
#     elif message.text == "играть":
#         # bot.send_message(message.chat.id,"давай начнем")
#         bot.register_next_step_handler(message,play)

# def play(message):
   
#     name1 = 'Вы'
#     name2 = "bot"
#     turn = 0
#     global a
#     a = 0
#     sweets = 200
#     max_sweet = 28
#     first_turn = random.choice([name1, name2])
#     flag = name1 if first_turn == name1 else name2
#     bot.send_message(message.chat.id,f"Кто ходит первым: {flag}")
#     while not 0<turn<max_sweet:

#         while sweets>0:
#             print(f"Ваш ход {flag}")

#             if flag == name1:
#                 bot.send_message(message.chat.id,"Введите кол-во конфет")
#                 # bot.register_next_step_handler(message,user_turn)
#                 turn = int(message.text)
#                 # while not 0<turn<max_sweet:
#                 #     bot.send_message(message.chat.id,f"Введите конфеты в диапазоне от 0 до {max_sweet}")
#                 #     bot.register_next_step_handler(message,user_turn)
                    
#                 sweets -= turn
#                 if sweets>0:
#                     bot.send_message(message.chat.id,f'конфет осталось - {sweets}')
#                 else:
#                     bot.send_message(message.chat.id,f'конфет осталось - 0')
#                 bot.send_message(message.chat.id,f"вы взяли {turn} конфет")
#                 sweets -= turn
#                 flag = name2 if flag == name1 else name1
#             else:
#                 turn = random.randint(1,max_sweet)
#                 bot.send_message(message.chat.id,f"bot взял {turn} конфет")
#                 sweets -= turn
#                 if sweets > 0:
#                     bot.send_message(message.chat.id,f'конфет осталось - {sweets}')
#                 else:
#                     bot.send_message(message.chat.id,'конфет осталось - 0')

#                 flag = name2 if flag == name1 else name1

#     winner = name2 if flag == name1 else name1
#     bot.send_message(message.chat.id,f"Поздравляем победил игрок {winner}")

# def user_turn(message):
#     global a
#     a = int(message.text)
    
    

   


# bot.infinity_polling()


