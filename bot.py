import telebot
from translate import translate, check_lang


TOKEN = "Token"
bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    users[message.from_user.id] = 'en'
    bot.reply_to(message, 'Hi :)')

@bot.message_handler(commands=['set_lang'])
def change_lang(message):
    lang = check_lang(message.text[9:].strip().lower())
    if (lang):
        users[message.from_user.id] = lang
        bot.reply_to(message, f'Language successfully changed to {lang}')
    elif lang == '':
        bot.reply_to(message, 'Please enter language after command')
    else:
        bot.reply_to(message, f'unable to find language {lang}')

@bot.message_handler(content_types = ['text'])
def translate_message(message):
    bot.reply_to(message, translate(message.text, dest_lang = users[message.from_user.id]))
    translate(message.text)

bot.infinity_polling()

