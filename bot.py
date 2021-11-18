import telebot
import config
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from today import td_forecast
from tomorrow import tm_forecast


# Bot initialisation
bot = telebot.TeleBot(config.TOKEN)


# Processing commands
@bot.message_handler(commands=['start'])
def commands(message):
    # Creating a reply markup
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Погода сьогодні')
    btn2 = KeyboardButton('Погода завтра')
    markup.add(btn1, btn2)

    msg = f'{message.from_user.first_name}, привіт!\n' \
          f'Я - <b>{bot.get_me().first_name}</b>, ' \
          f'бот для отримання погоди в Києві☺'
    bot.send_message(message.chat.id, msg, reply_markup=markup,
                     parse_mode='html')


# Processing text messages
@bot.message_handler(content_types=['text'])
def texts(message):
    if message.text in ('Погода сьогодні', 'с'):
        bot.send_message(message.chat.id, td_forecast)
    elif message.text in ('Погода завтра', 'з'):
        bot.send_message(message.chat.id, tm_forecast)
    else:
        bot.send_message(message.chat.id, 'Я не знаю що відповісти😞')


# Running
bot.polling(none_stop=True)
