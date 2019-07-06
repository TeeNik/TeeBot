import requests
import telebot
import sys
import db
from answer_reason import AnswerReason
from answer_reason import HELP_TEXT


token = sys.argv[1];
bot = telebot.TeleBot(token)

updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
files_path = '/TeeBot/pics/'

botDB = db.TeeBotDB()
answer_reason = AnswerReason.NONE
theme_list = botDB.get_themes_list()


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(commands=["meme"])
def send_meme(message):
    try:
        chat_id = message.chat.id

        text = str(message.json['text'])
        params = text.split(" ")
        if len(params) > 1 and params[1] in theme_list:
            filename = botDB.get_meme_by_theme(params[1])
        else:
            filename = botDB.get_random_meme()
        photo = open(f'{files_path}{filename}', 'rb')
        bot.send_photo(chat_id, photo)
    except Exception as e:
        bot.send_message(chat_id, "Эксепшон!!!!\n")
        bot.send_message(chat_id, e)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, message)

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'{files_path}{file_info.file_path}'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(chat_id, "Картинка сохранена")
    except Exception as e:
        bot.send_message(chat_id, e)


@bot.message_handler(commands=['show_themes'])
def handle_show_themes(message):
    text = 'Темы мемов:\n'
    for theme in theme_list:
        text += f"{theme}\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("\n")
    print(message)
    pass


bot.polling()
