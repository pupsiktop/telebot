import telebot #импорт библиотеки
from wiki import Wikipedia as w
from keyboard import markup, markup_menu

API_TOKEN = '8387377639:AAE-SpmVUAPVp90YfCQ8vruB5gXIYAEUUhY'
photo = open('logo.png', 'rb')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start', 'hello'])
def start(message):
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, 'Hello! what you want to search?', reply_markup=markup_menu)
    bot.register_next_step_handler(message, search)
def search(message):
    title, content = w.search(message.text)
    if title is not None and content is not None:
        bot.send_message(message.chat.id, 'the article' + title)
        bot.send_message(message.chat.id, content, reply_markup=markup)
        bot.register_next_step_handler(message, restart)
    else:
        print('there isnt any articles')

def restart(message):
    if message.text.lower() == 'restart':
        mssg = bot.send_message(message.chat.id, 'against search, enter the word')
        bot.register_next_step_handler(mssg, search)
    else:
         bot.send_message(message.chat.id, 'thanks for using')






#def hello(message):
    #bot.reply_to(message, 'Нет, не надо, пожалуйста')
    #bot.send_message(message.chat.id,f'**start ')
    #bot.register_next_step_handler(message, register)

#def register(message):
#    bot.send_message(message.chat.id, f'**the link was sent on your mail {message.text}**')

#@bot.message_handler()
#def small_talk(message):
#    if message.text.lower() == 'hello':
#        bot.send_message(message.chat.id, 'hello!')
#    elif message.text.lower() == 'how are you?':
#        bot.send_message(message.chat.id, 'all good!')
#    elif message.text.lower() == 'bye-bye':
#        bot.send_message(message.chat.id, 'bye!')
#
#
bot.polling() #мониторить входящее сообщение