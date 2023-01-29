import telebot
from telebot import types
import random
from random import randint
bot = telebot.TeleBot("5804587400:AAELkmE4RmkQKUl6745HozMTO-DfSZfH0d4")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"/button")
    
@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("узнать правила игры")
    but2 = types.KeyboardButton("играть")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

@bot.message_handler(content_types = "text")
def controller(message):
    print(message.text)
    if message.text == "узнать правила игры":
        bot.send_message(
            message.chat.id,
            "На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга."
            "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет." 
            "Все конфеты оппонента достаются сделавшему последний ход."
        )
    elif message.text == "играть":
        # bot.send_message(message.chat.id,"давай начнем")
        bot.register_next_step_handler(message,play)

def play(message):
   
    name1 = 'Вы'
    name2 = "bot"
    turn = 0
    global a
    a = 0
    sweets = 200
    max_sweet = 28
    first_turn = random.choice([name1, name2])
    flag = name1 if first_turn == name1 else name2
    bot.send_message(message.chat.id,f"Кто ходит первым: {flag}")
    while not 0<turn<max_sweet:

        while sweets>0:
            print(f"Ваш ход {flag}")

            if flag == name1:
                bot.send_message(message.chat.id,"Введите кол-во конфет")
                # bot.register_next_step_handler(message,user_turn)
                turn = int(message.text)
                # while not 0<turn<max_sweet:
                #     bot.send_message(message.chat.id,f"Введите конфеты в диапазоне от 0 до {max_sweet}")
                #     bot.register_next_step_handler(message,user_turn)
                    
                sweets -= turn
                if sweets>0:
                    bot.send_message(message.chat.id,f'конфет осталось - {sweets}')
                else:
                    bot.send_message(message.chat.id,f'конфет осталось - 0')
                bot.send_message(message.chat.id,f"вы взяли {turn} конфет")
                sweets -= turn
                flag = name2 if flag == name1 else name1
            else:
                turn = random.randint(1,max_sweet)
                bot.send_message(message.chat.id,f"bot взял {turn} конфет")
                sweets -= turn
                if sweets > 0:
                    bot.send_message(message.chat.id,f'конфет осталось - {sweets}')
                else:
                    bot.send_message(message.chat.id,'конфет осталось - 0')

                flag = name2 if flag == name1 else name1

    winner = name2 if flag == name1 else name1
    bot.send_message(message.chat.id,f"Поздравляем победил игрок {winner}")

def user_turn(message):
    global a
    a = int(message.text)
    
    

   


bot.infinity_polling()


        
# while not 0<turn<max_sweet:

# def pve_s():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход"))

#     first_turn = random.choice([name1, name2])
#     flag = name1 if first_turn == name1 else name2

#     while sweets>0:
#         print(f"Ваш ход {flag}")

#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))

#             while not 0<turn<max_sweet:
#                 print("Введите конфеты в диапазоне от 0 до", max_sweet)
#                 turn = int(input("введите желаемое количество конфет для взятия- "))

#             sweets -= turn
#             if sweets>0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')

#             flag = name2 if flag == name1 else name1
#         else:
#             turn = random.randint(1,max_sweet)
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')

#             flag = name2 if flag == name1 else name1

#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")



# def pve_smart():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход"))

#     first_turn = random.choice([name1, name2])
#     flag = name1 if first_turn == name1 else name2

#     while sweets>0:
#         print(f"Ваш ход {flag}")

#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))

#         else:
#             if sweets == max_sweet:
#                 turn = sweets
#             elif sweets%max_sweet==0:
#                 turn = max_sweet-1
#             else:
#                 turn = sweets%max_sweet-1
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')

#             flag = name2 if flag == name1 else name1

#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")

# pve_smart()
