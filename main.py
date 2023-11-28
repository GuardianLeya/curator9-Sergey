import telebot

bot = telebot.TeleBot('6894159462:AAFEuBWt27twreaP35d5hEOPxISwR9kzw8w')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'I drive. Поехали, пиши: /drive', parse_mode='Markdown')


@bot.message_handler(commands=['drive'])
def drive(message):
    bot.send_message(message.chat.id,
                     '[Let`s drive \nЕсли хочешь быть как я, пиши: /literally_me] \n(https://www.youtube.com/watch?v=ruawVE5GwM8)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['literally_me'])
def literally_me(message):
    bot.send_message(message.chat.id,
                     'Ну вот теперь ты настоящий сигма \n(https://www.youtube.com/watch?v=2Vcy8huku_Q)')


bot.infinity_polling()