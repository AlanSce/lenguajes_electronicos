# En la misma carpeta de este código debe estar el código bases que se encuentra en el repositorio en la carpeta "mongo"

import os
import telebot
from base import Storage

BOT_TOKEN = '6995767185:AAF0XimjKhQxXhb1PgvjfCD1HvAy-8LBmrs'

bot = telebot.TeleBot(BOT_TOKEN)

uri = "mongodb://localhost:27017/"
db = "madero"
coll = "clases"

storage = Storage(uri, db, coll)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenido")

@bot.message_handler(commands=['materias'])
def send_materias(message):
    materias = storage.find()
    mensaje = ""
    for materia in materias:
        mensaje += f"Materia: {materia['Materia']}"
        mensaje += "\n"
    bot.reply_to(message, mensaje)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

bot.infinity_polling()
