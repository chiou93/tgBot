import telebot
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(commands=['get_info', 'info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup() #telebot.types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data = 'no')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Желаешь узнать  информацию о себе?', reply_markup = markup_inline)


@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Мой ник')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Выбери действие:', reply_markup = markup_reply)
    elif call.data == 'no':
        client.send_message(call.message.chat.id, 'Хорошо')
    
    


@client.message_handler(content_types=['text']) # client.message_handler-обращаемся к боту: message_handler-обработчик сообщений: content_types=['text']-тип сообщения
def get_text(message): # def get_text()-функция, которая будет выполняться при получении текстового сообщения
    if message.text.lower() == 'привет': # message.text.lower()-приводим к нижнему регистру
        client.send_message(message.chat.id, 'Привет, человек!') # client.send_message(message.chat.id, 'Привет, человек!')-отправляем сообщение: message.chat.id-идентификатор чата, 'Привет, человек!'-сообщение
    elif message.text.lower() == 'как дела?':
        client.send_message(message.chat.id, 'Все хорошо, как у тебя?❤️')
    elif message.text.lower() == 'хорошо':
        client.send_message(message.chat.id, 'Отлично!😊')
    elif message.text.lower() == 'пока':
        client.send_message(message.chat.id, 'До встречи!👋')
    elif message.text.lower() == '/start':
        client.send_message(message.chat.id, 'Привет, человек!')
    elif message.text.lower() == '/help':
        client.send_message(message.chat.id, 'Чтобы узнать информацию о себе, набери /info.')
    elif message.text.lower() == '/info':
        get_user_info(message)
    elif message.text == 'Мой ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}') #'Твой id: ' + str(message.chat.id)
    elif message.text == 'Мой ник':
        client.send_message(message.chat.id, f'Your name: {message.from_user.first_name} {message.from_user.last_name}') #'Твой ник: ' + message.chat.username




client.polling(none_stop=True) # client.polling(none_stop=True)-бесконечный цикл, который будет получать сообщения от пользователя: interval=0-интервал между запросами к серверу