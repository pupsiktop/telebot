from telebot.types import ReplyKeyboardMarkup, KeyboardButton

markup = ReplyKeyboardMarkup()
btn1 = (KeyboardButton('Restart'))
btn2 = (KeyboardButton('Clear'))
btn3 = (KeyboardButton('About'))
btn4 = (KeyboardButton('exit'))
markup.row(btn1, btn3)
markup.row(btn2, btn4)

markup_menu = ReplyKeyboardMarkup()
btn5 = (KeyboardButton('Restart'))
btn6 = (KeyboardButton('Menu'))
markup_menu.row(btn5, btn6)
