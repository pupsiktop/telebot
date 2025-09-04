import telebot #импорт библиотеки

API_TOKEN = '8387377639:AAE-SpmVUAPVp90YfCQ8vruB5gXIYAEUUhY'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start', 'hello'])

def hello(message):
    #bot.reply_to(message, 'Нет, не надо, пожалуйста')
    bot.send_message(message.chat.id,f'**start ')
    #bot.register_next_step_handler(message, register)

#def register(message):
#    bot.send_message(message.chat.id, f'**the link was sent on your mail {message.text}**')

@bot.message_handler()
def small_talk(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'hello!')
    elif message.text.lower() == 'how are you?':
        bot.send_message(message.chat.id, 'all good!')
    elif message.text.lower() == 'bye-bye':
        bot.send_message(message.chat.id, 'bye!')


bot.polling() #мониторить входящее сообщение