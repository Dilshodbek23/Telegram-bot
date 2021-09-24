from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '2032423523:AAH_Nu2fBTS83yReh_xSI84t10jKhwOBlM8'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer = "Howdy, how are you doing?"
    answer += "\nPlease enter your text"
    bot.reply_to(message, answer)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))
    
# ================We could also write it like this.============================
#
#     if msg.isascii():
#         answer = to_cyrillic(msg)
#     else:
#         answer = to_latin(msg)
#     bot.reply_to(message, answer)
# =============================================================================
    
    
bot.polling()


