import telebot
from telebot import types
import random

bot = telebot.TeleBot('5903145927:AAFDqsEZFDgKnDBugOUJtsNkj-v2sKPVv4o')

def med_test(message):
    if message.text == 'Тест на зрения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn10 = types.KeyboardButton("Да")
        btn20 = types.KeyboardButton("Нет")
        markup.add(btn10, btn20)
        bot.send_message(message.chat.id, 'вы гей', reply_markup=markup)

    if message.chat.type == 'private':
        if message.text == "Да":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton("Нет")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, reply_markup=markup)
            bot.send_message(message.chat.id, f'Вы на гей')

    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Вы не гей', reply_markup=markup)



        bot.send_message(message.chat.id, f'Вы на гей')