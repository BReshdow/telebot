import telebot
import config

# Bot initialisation
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler()
def start():
    pass


# Running
bot.polling(none_stop=True)
