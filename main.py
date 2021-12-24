from logging import Logger
import telebot

bot = telebot.TeleBot("5033625021:AAHcu9cX8wHg17abSyFlaKpIfOOlXfuk4nQ")


def verify(message):
        resp = message
        respRetrive = resp.json()
        print(respRetrive)
        
@bot.message_handler(func = verify)
def send_welcome(message):
	bot.reply_to(message, "Olá, tudo bem? Se você está aqui você deve conhecer minha rede do Linkedin.\nConfira o GitHub desse Código :  https://github.com/albuquerquealdry")

bot.polling()