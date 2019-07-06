import requests
import telebot

token = "877998317:AAFNcXuKLX3EU2FQpMjsiko26KAyIXlBoyA";
bot = telebot.TeleBot(token)

updates_url = f"https://api.telegram.org/bot{token}/getUpdates"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Слышь, пидор, когда долг отдашь?")


@bot.message_handler(commands=["meme"])
def send_meme(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "It's Britney BITCH!")
    # updates = bot.get_updates()
    # print(updates)
    photo = open('/TeeBot/pics/meme.jpg', 'rb')
    # chat_id = 1
    bot.send_photo(chat_id, photo)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("\n")
    print(message)
    bot.send_sticker()
    bot.reply_to(message, message.text)


bot.polling()
