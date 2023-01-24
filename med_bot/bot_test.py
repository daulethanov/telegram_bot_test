import telebot
from telebot import types
import random

bot = telebot.TeleBot('5790864444:AAH2Q_AiQmnrV12uEoW1zxzVi_G4xVyXFb4')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📣Тест на беременность")
    btn2 = types.KeyboardButton("🔔Библиотека для улучшения здровье")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text='''Здраствуйте дорогой пользователь если вы чувствуете себя психически больным то предлагаю вам пройти тест на психическую устойчивость или почитать полезные статьи о психологическом здоровье'''.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def test(message):
    global points

# Выбор теста
    if message.text == '📣Тест на беременность' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Тест на беременность")
        btn2 = types.KeyboardButton("Тест иммуной системы")
        btn3 = types.KeyboardButton("Тест: знаете ли вы, как вести здоровый образ жизни?")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='👾Тесты на ваш выбор:  '.format(message.from_user), reply_markup=markup)
#Тест на риск развития диабета

    if message.text == 'Тест на беременность':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Был")
        btn2 = types.KeyboardButton("Не был")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Был ли у вас вагинальный секс после последней менструации?', reply_markup=markup)

    if message.chat.type == 'private':
        if message.text == "Не был":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton("Нет")

            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Было ли попадение спермы во влагалище при других видах секса? ', reply_markup=markup)

        if message.text == 'Был':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не использовали")
            btn2 = types.KeyboardButton("Контрацептив")
            btn3 = types.KeyboardButton("Противозачаточные препараты")
            btn4 = types.KeyboardButton("Внутриматочное противозачаточное средство")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text='Использовали ли вы срдества защиты?', reply_markup=markup)

        elif message.text == 'Нет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Если в вас не попадала семенная жидкость во время вагинального секса или других сексуальных активностей - Вы НЕ можете быть беременны',reply_markup=markup)

        if message.text == 'Не использовали':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, был")
            btn2 = types.KeyboardButton("Нет, не был")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Был ли у вас незащищенный вагинальный секс в течении последних 5 дней?', reply_markup=markup)

        if message.text == 'Да, был':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Наблюдали")
            btn2 = types.KeyboardButton("Не наблюдали")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Наблюдали ли вы признаки ранней беременности?', reply_markup=markup)

        if message.text == "Нет, не был":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text='Поздравляю вы не беременны!', reply_markup=markup)

        if message.text == 'Наблюдали':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Не наблюдали':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Контрацептив':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, наблюдали")
            btn2 = types.KeyboardButton("Нет, не наблюдали")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Наблюдали ли вы признаки ранней беременности?', reply_markup=markup)

        if message.text == 'Да, наблюдали':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Нет, не наблюдали':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Противозачаточные препараты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, наблюдали  ")
            btn2 = types.KeyboardButton("Нет, не наблюдали  ")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Наблюдали ли вы признаки ранней беременности?', reply_markup=markup)

        if message.text == 'Да, наблюдали  ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Нет, не наблюдали  ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!',reply_markup=markup)

        if message.text == "Внутриматочное противозачаточное средство":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, наблюдали   ")
            btn2 = types.KeyboardButton("Нет, не наблюдали   ")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Наблюдали ли вы признаки ранней беременности?', reply_markup=markup)

        if message.text == 'Да, наблюдали   ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

        if message.text == 'Нет, не наблюдали   ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Cпасибо')
            btn2 = types.KeyboardButton('Выбрать другой тест')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Рекомендуем вам обратиться к врачу!', reply_markup=markup)

#Тест: знаете ли вы, как вести здоровый образ жизни?
    #1
    if message.text == 'Тест: знаете ли вы, как вести здоровый образ жизни?':
        points = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заводите будильник")
        btn2 = types.KeyboardButton("Доверяете внутреннему голосу")
        btn3 = types.KeyboardButton("Полагаетесь на случай")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Если утром вам надо встать пораньше, вы?', reply_markup=markup)

    if message.chat.type == 'private':
        #2
        if message.text == "Заводите будильник":
            points += 15
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Каждый день")
            btn2 = types.KeyboardButton("Иногда")
            btn3 = types.KeyboardButton("Редко")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Как в суете учебных дел и обязанностей у вас выдается возможность немножко пошутить и посмеяться с коллегами?', reply_markup=markup)

        elif message.text == 'Доверяете внутреннему голосу':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Каждый день")
            btn2 = types.KeyboardButton("Иногда")
            btn3 = types.KeyboardButton("Редко")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Как в суете учебных дел и обязанностей у вас выдается возможность немножко пошутить и посмеяться с коллегами?', reply_markup=markup)

        elif message.text == 'Полагаетесь на случай':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Каждый день")
            btn2 = types.KeyboardButton("Иногда")
            btn3 = types.KeyboardButton("Редко")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Как в суете учебных дел и обязанностей у вас выдается возможность немножко пошутить и посмеяться с коллегами?', reply_markup=markup)
        #3
        if message.text == "Каждый день":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не учусь")
            btn2 = types.KeyboardButton("До 1 часа")
            btn3 = types.KeyboardButton("Более 1 часа")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Надолго ли вы обычно задерживаетесь после занятий?', reply_markup=markup)

        elif message.text == 'Иногда':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не учусь")
            btn2 = types.KeyboardButton("До 1 часа")
            btn3 = types.KeyboardButton("Более 1 часа")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Надолго ли вы обычно задерживаетесь после занятий?', reply_markup=markup)

        elif message.text == 'Редко':
            points += 4
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не учусь")
            btn2 = types.KeyboardButton("До 1 часа")
            btn3 = types.KeyboardButton("Более 1 часа")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Надолго ли вы обычно задерживаетесь после занятий?', reply_markup=markup)
        #4
        if message.text == "Не учусь":
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("По окончанию всех дел")
            btn2 = types.KeyboardButton("По настроению")
            btn3 = types.KeyboardButton("Всегда примерно в одно и то же время")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Когда вы ложитесь спать?', reply_markup=markup)

        elif message.text == 'До 1 часа':
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("По окончанию всех дел")
            btn2 = types.KeyboardButton("По настроению")
            btn3 = types.KeyboardButton("Всегда примерно в одно и то же время")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Когда вы ложитесь спать?', reply_markup=markup)

        elif message.text == 'Более 1 часа':
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("По окончанию всех дел")
            btn2 = types.KeyboardButton("По настроению")
            btn3 = types.KeyboardButton("Всегда примерно в одно и то же время")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Когда вы ложитесь спать?', reply_markup=markup)
        #5
        if message.text == "По окончанию всех дел":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Возможность встряхнуться и отвлечься от забот")
            btn2 = types.KeyboardButton("Потеря времени и денег")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Встреча с друзьями и прием гостей для вас – это?', reply_markup=markup)

        elif message.text == 'По настроению':
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Возможность встряхнуться и отвлечься от забот")
            btn2 = types.KeyboardButton("Потеря времени и денег")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Встреча с друзьями и прием гостей для вас – это?', reply_markup=markup)

        elif message.text == 'Всегда примерно в одно и то же время':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Возможность встряхнуться и отвлечься от забот")
            btn2 = types.KeyboardButton("Потеря времени и денег")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Встреча с друзьями и прием гостей для вас – это?', reply_markup=markup)
        #6
        if message.text == 'Возможность встряхнуться и отвлечься от забот':
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Спасибо")
            btn2 = types.KeyboardButton("Выбрать другой тест")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f'Вы введете здоровый образ жизни на {points}%', reply_markup=markup)

        elif message.text == 'Потеря времени и денег':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Спасибо")
            btn2 = types.KeyboardButton("Выбрать другой тест")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f'Вы введете здоровый образ жизни на {points}%', reply_markup=markup)


#Тест иммуной системы

    if message.text == 'Тест иммуной системы':
        points = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Бывает, но я стараюсь расслабиться")
        btn2 = types.KeyboardButton("Я часто нервничаю")
        btn3 = types.KeyboardButton("Почти никогда")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Как часто у вас бывает стресс?', reply_markup=markup)

    if message.chat.type == 'private':
       #1
        if message.text == "Бывает, но я стараюсь расслабиться":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Менее 3 раз")
            btn2 = types.KeyboardButton("От 3 до 6 раз")
            btn3 = types.KeyboardButton("Более 6 раз")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Сколько раз в году вы простужаетесь?', reply_markup=markup)

        elif message.text == 'Я часто нервничаю':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Менее 3 раз")
            btn2 = types.KeyboardButton("От 3 до 6 раз")
            btn3 = types.KeyboardButton("Более 6 раз")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Сколько раз в году вы простужаетесь?', reply_markup=markup)

        elif message.text == 'Почти никогда':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Менее 3 раз")
            btn2 = types.KeyboardButton("От 3 до 6 раз")
            btn3 = types.KeyboardButton("Более 6 раз")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Сколько раз в году вы простужаетесь?', reply_markup=markup)

        #2
        if message.text == "Менее 3 раз":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Остаюсь лечиться дома, незачем издеваться над организмом, здоровье дороже, его потом не купишь")
            btn2 = types.KeyboardButton("Придется работать из дома сквозь кашель и температуру, что поделать")
            btn3 = types.KeyboardButton("Надо идти на работу, не дойду — так доползу")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Если вы умудрились заболеть и, что называется, слегли — останетесь в постели или героически пойдете на работу?', reply_markup=markup)

        elif message.text == 'От 3 до 6 раз':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Остаюсь лечиться дома, незачем издеваться над организмом, здоровье дороже, его потом не купишь")
            btn2 = types.KeyboardButton("Придется работать из дома сквозь кашель и температуру, что поделать")
            btn3 = types.KeyboardButton("Надо идти на работу, не дойду — так доползу")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Если вы умудрились заболеть и, что называется, слегли — останетесь в постели или героически пойдете на работу?', reply_markup=markup)

        elif message.text == 'Более 6 раз':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Остаюсь лечиться дома, незачем издеваться над организмом, здоровье дороже, его потом не купишь")
            btn2 = types.KeyboardButton("Придется работать из дома сквозь кашель и температуру, что поделать")
            btn3 = types.KeyboardButton("Надо идти на работу, не дойду — так доползу")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Если вы умудрились заболеть и, что называется, слегли — останетесь в постели или героически пойдете на работу?', reply_markup=markup)

        #3
        if message.text == "Надо идти на работу, не дойду — так доползу":
            points += 10

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, есть")
            btn2 = types.KeyboardButton("Нету")
            btn3 = types.KeyboardButton("Не совсем")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Есть ли у вас хронические заболевания?', reply_markup=markup)

        elif message.text == 'Остаюсь лечиться дома, незачем издеваться над организмом, здоровье дороже, его потом не купишь':
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, есть")
            btn2 = types.KeyboardButton("Нету")
            btn3 = types.KeyboardButton("Не совсем")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Есть ли у вас хронические заболевания?', reply_markup=markup)

        elif message.text == 'Придется работать из дома сквозь кашель и температуру, что поделать':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, есть")
            btn2 = types.KeyboardButton("Нету")
            btn3 = types.KeyboardButton("Не совсем")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Есть ли у вас хронические заболевания?', reply_markup=markup)

            # 4
        if message.text == "Да, есть":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да принимаю")
            btn2 = types.KeyboardButton("Не принимаю")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Принимаете ли вы какие-нибудь лекарства регулярно?',
                                 reply_markup=markup)

        elif message.text == 'Нету':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да принимаю")
            btn2 = types.KeyboardButton("Не принимаю")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Принимаете ли вы какие-нибудь лекарства регулярно?',
                                 reply_markup=markup)

        elif message.text == 'Не совсем':
            points += 5
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да принимаю")
            btn2 = types.KeyboardButton("Не принимаю")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Принимаете ли вы какие-нибудь лекарства регулярно?',
                                 reply_markup=markup)

            # 5
        if message.text == "Да принимаю":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, курю")
            btn2 = types.KeyboardButton("Не курю")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Курите ли вы?',
                                 reply_markup=markup)

        elif message.text == 'Не принимаю':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, курю")
            btn2 = types.KeyboardButton("Не курю")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Курите ли вы?',
                                 reply_markup=markup)

            # 6
        if message.text == "Да, курю":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не пью")
            btn2 = types.KeyboardButton("Пью")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Алкоголь употребляете?',
                                 reply_markup=markup)

        elif message.text == 'Не курю':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Не пью")
            btn2 = types.KeyboardButton("Пью")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Алкоголь употребляете?',
                                 reply_markup=markup)

            # 7
        if message.text == "Пью":
            points += 10
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, занимаюсь")
            btn2 = types.KeyboardButton("Не занимаюсь")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Часто ли вы занимаетесь спортом?',
                                 reply_markup=markup)

        elif message.text == 'Не пью':
            points += 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, занимаюсь")
            btn2 = types.KeyboardButton("Не занимаюсь")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                                 'Часто ли вы занимаетесь спортом?',
                                 reply_markup=markup)
            #8
        if message.text == "Да, занимаюсь":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Спасибо")
            btn2 = types.KeyboardButton("Выбрать другой тест")
            markup.add(btn1, btn2)
            points += 0
            bot.send_message(message.chat.id, f'Вы не здоровы на {points}%', reply_markup=markup)

        elif message.text == 'Не занимаюсь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Спасибо")
            btn2 = types.KeyboardButton("Выбрать другой тест")
            markup.add(btn1, btn2)
            points += 10
            bot.send_message(message.chat.id, f'Вы не здоровы на {points}%', reply_markup=markup)
        # окончание теста

        if message.text == 'Спасибо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Выбрать другой тест")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Выбрать другой тест':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # btn1 = types.KeyboardButton("Тест на риск развития диабета ")
            btn2 = types.KeyboardButton("Тест иммуной системы")
            btn3 = types.KeyboardButton("Тест: знаете ли вы, как вести здоровый образ жизни?")
            markup.add(btn2, btn3)
            bot.send_message(message.chat.id, text='👾Тесты на ваш выбор:  '.format(message.from_user),
                             reply_markup=markup)





    # Полезные источники
    if message.text == '🔔Библиотека для улучшения здровье':

        youtube = [
          'https://www.youtube.com/watch?v=Elvt-w_TKSU',
            'https://www.youtube.com/watch?v=XYr_NxCrvUQ',
            'https://www.youtube.com/watch?v=ROXRTVDYZec',
            'https://kz.iherb.com/blog?p=2',
            'https://4brain.ru/blog/sposoby-podderzhanija-zdorovja-na-kazhdyj-den/',
            'https://rsv.ru/blog/7-sposobov-razvit-ejdeticheskuyu-pamyat/'

        ]
        a = random.choice(youtube)

        bot.send_message(message.chat.id, a)


bot.polling()

