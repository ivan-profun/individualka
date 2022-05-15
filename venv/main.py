import telebot
from telebot import types

bot = telebot.TeleBot("5241900918:AAFNEti3E8vEC6MVwfbP9a4yxL87yY9Zemc")


infoTime = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


@bot.message_handler(commands=['start', 'info'])
def menu(message):
    if (message.text == '/start'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        surrender = types.KeyboardButton('Сдать костюм')
        markup.add(surrender)
        bot.send_message(message.chat.id, 'Привет, {0.first_name}! Чем могу помочь?'.format(message.from_user), reply_markup=markup)

    elif (message.text == '/info'):
        bot.send_message(message.chat.id, 'Вот вся информация:')
        bot.send_message(message.chat.id, 'Капельки: Пн:' + str(infoTime[0][0]) + ' Вт:' + str(infoTime[0][1]) + ' Ср:' + str(infoTime[0][2]) + ' Чт:' + str(infoTime[0][3]) + ' Пт:' + str(infoTime[0][4]) + ' Сб:' + str(infoTime[0][5]))
        bot.send_message(message.chat.id, 'Звонкий дождь: Пн:' + str(infoTime[1][0]) + ' Вт:' + str(infoTime[1][1]) + ' Ср:' + str(infoTime[1][2]) + ' Чт:' + str(infoTime[1][3]) + ' Пт:' + str(infoTime[1][4]) + ' Сб:' +str(infoTime[1][5]))
        bot.send_message(message.chat.id, 'StarKids: Пн:' + str(infoTime[2][0]) + ' Вт:' + str(infoTime[2][1]) + ' Ср:' + str(infoTime[2][2]) + ' Чт:' + str(infoTime[2][3]) + ' т:' + str(infoTime[2][4]) + ' Сб:' + str(infoTime[2][5]))
        bot.send_message(message.chat.id, 'Радуга: Пн:' + str(infoTime[3][0]) + ' Вт:' + str(infoTime[3][1]) + ' Ср:' + str(infoTime[3][2]) + ' Чт:' + str(infoTime[3][3]) + ' Пт:' + str(infoTime[3][4]) + ' Сб:' + str(infoTime[3][5]))
        bot.send_message(message.chat.id, 'Кадры: Пн:' + str(infoTime[4][0]) + ' Вт:' + str(infoTime[4][1]) + ' Ср:' + str(infoTime[4][2]) + ' Чт:' + str(infoTime[4][3]) + ' Пт:' + str(infoTime[4][4]) + ' Сб:' + str(infoTime[4][5]))
        bot.send_message(message.chat.id, 'Выше радуги: Пн:' + str(infoTime[5][0]) + ' Вт:' + str(infoTime[5][1]) + ' Ср:' + str(infoTime[5][2]) + ' Чт:' + str(infoTime[5][3]) + ' Пт:' + str(infoTime[5][4]) + ' Сб:' + str(infoTime[5][5]))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        gotoStart = types.KeyboardButton('Вернуться в начало')
        markup.add(gotoStart)
        bot.send_message(message.chat.id, 'Хочешь вернуться к началу?', reply_markup=markup)
        if (message.text == 'Вернуться в начало'):
            bot.send_message(message.text.id, menu(message))




@bot.message_handler(content_types=['text'])
def fun1(message):
    if (message.text == 'Сдать костюм'):
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        group1 = types.KeyboardButton('Капельки')
        group2 = types.KeyboardButton('Звонкий дождь')
        group3 = types.KeyboardButton('StarKids')
        group4 = types.KeyboardButton('Радуга')
        group5 = types.KeyboardButton('Кадры')
        group6 = types.KeyboardButton('Выше радуги')
        markup1.add(group1, group2, group3, group4, group5, group6)
        bot.send_message(message.chat.id, "Костюм какой группы хотите сдать?", reply_markup=markup1)

    whatGroup = 0  # выбор группы

    #if (message.text == 'Костюм какой группы хотите сдать?'):
    if (message.text == 'Капельки'):
        whatGroup = 1

    elif (message.text == 'Звонкий дождь'):
        whatGroup = 2

    elif (message.text == 'StarKids'):
        whatGroup = 3

    elif (message.text == 'Радуга'):
        whatGroup = 4

    elif (message.text == 'Кадры'):
        whatGroup = 5

    elif (message.text == 'Выше радуги'):
        whatGroup = 6

    if (whatGroup != 0):
        markupTime = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        group1 = types.KeyboardButton('Понедельник: с 15:00 до 20:00')
        group2 = types.KeyboardButton('Вторник: с 15:00 до 20:00')
        group3 = types.KeyboardButton('Среда: с 15:00 до 20:00')
        group4 = types.KeyboardButton('Четверг: с 15:00 до 20:00')
        group5 = types.KeyboardButton('Пятница: с 15:00 до 20:00')
        group6 = types.KeyboardButton('Суббота: с 15:00 до 19:00')
        markupTime.add(group1, group2, group3, group4, group5, group6)
        bot.send_message(message.chat.id, "В какой день на этой неделе вы хотите сдать костюм?", reply_markup=markupTime)

        whatTime = 0  # выбор времени

        if message.text == 'Понедельник: с 15:00 до 20:00':
            whatTime = 1

        elif message.text == 'Вторник: с 15:00 до 20:00':
            whatTime = 2

        elif message.text == 'Среда: с 15:00 до 20:00':
            whatTime = 3

        elif message.text == 'Четверг: с 15:00 до 20:00':
            whatTime = 4

        elif message.text == 'Пятница: с 15:00 до 20:00':
            whatTime = 5

        elif message.text == 'Суббота: с 15:00 до 19:00':
            whatTime = 6

        if (whatTime != 0):
            bot.send_message(message.chat.id, 'Всё отмечено!')

            if (whatTime == 1):
                infoTime[0][0] += 1

            elif (whatTime == 2):
                infoTime[0][1] += 1

            elif (whatTime == 3):
                infoTime[0][2] += 1

            elif (whatTime == 4):
                infoTime[0][3] += 1

            elif (whatTime == 5):
                infoTime[0][4] += 1

            elif (whatTime == 6):
                infoTime[0][5] += 1

            #if (whatTime != 0):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            surrender = types.KeyboardButton('Сдать костюм')
            markup.add(surrender)
            bot.send_message(message.chat.id, 'Хотите ещё сдать костюм?')
            bot.send_message(message.chat.id, fun1(message))

            if (message.text == 'Сдать костюм'):
                markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                surrender = types.KeyboardButton('Начать с начала!')
                markup3.add(surrender)
                bot.send_message(message.chat.id, 'Хотите начать с начала?', reply_markup=markup3)
                if (message.text == 'Начать с начала!'):
                    bot.send_message(message.chat.id, menu())

                bot.send_message(message.chat.id, 'Чтоб вернуться нажмите на /start')















# для постоянной работы бота ##########
while(1):
    bot.polling(none_stop=True)
#######################################