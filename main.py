import time
import telebot
import datetime
from telebot import types

BOT_TOKEN = "5515316713:AAGJOcVOiaGZ3SMqY9DTRPqkbBk5X8d4JFo"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

OWNER = ["5473137780"]

@bot.message_handler(commands=['start', 'help'])
def helpstr(message):
    expiry_date = datetime.datetime.now()
    
    bot.reply_to(message, f"""<b>Hello <a href='https://t.me/{message.from_user.username}'><b>{message.from_user.first_name}</b> 👋</a>\nWelcome to 𝐒𝐈𝐓𝐄 𝐇𝐔𝐍𝐓𝐄𝐑 bot\nTo see all the commands send /cmds \nYour ID:<code> {message.from_user.id} </code>\nTime: <code>{expiry_date.strftime('%Y-%m-%d %H:%M:%S')}</code>\n\n - Bot by:</b> <a href='https://t.me/KV_ON'><b>𓆩 O҉M҉A҉R҉ F҉O҉U҉D҉A҉ 𓆪</b></a>""",
        disable_web_page_preview=True,
        parse_mode="HTML"
    )
    
if __name__ == '__main__':
    bot.polling()
