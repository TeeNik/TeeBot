import requests
import telebot
import sys
import db
from answer_reason import AnswerReason
import answer_reason

token = sys.argv[1];
bot = telebot.TeleBot(token)

updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
files_path = '/TeeBot/pics/'

botDB = db.TeeBotDB()
reason_to_answer = AnswerReason.NONE
theme_list = botDB.get_themes_list()


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    photo = open(f'{files_path}memologist.png', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id, answer_reason.HELP_TEXT)


def get_command_params(message):
    text = str(message.json['text'])
    return text.split(" ")


@bot.message_handler(commands=["meme"])
def send_meme(message):
    try:
        chat_id = message.chat.id
        themes = botDB.get_themes_list()
        params = get_command_params(message)

        if len(params) > 1 and params[1] in themes:
            filename = botDB.get_meme_by_theme(params[1])
        else:
            filename = botDB.get_random_meme()
        photo = open(f'{files_path}{filename}', 'rb')
        bot.send_photo(chat_id, photo)
    except Exception as e:
        bot.send_message(chat_id, "Эксепшон!!!!\n")
        bot.send_message(chat_id, e)


@bot.message_handler(commands=['add_meme'])
def handle_add_meme(message):
    if message.chat.type == 'group':
        bot.send_message(message.chat.id, answer_reason.NOT_ABLE_IN_GROUP)
        return

    global reason_to_answer
    reason_to_answer = AnswerReason.ADD_FILE
    send_reply_photo(message.chat.id)


@bot.message_handler(content_types=['document'])
def handle_docs_file(message):
    try:
        chat_id = message.chat.id

        if message.reply_to_message is None:
            bot.send_message(chat_id, answer_reason.SO_FUNNY)

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        filename = str(message.document.file_name)
        print(filename)
        src = f'{files_path}{filename}'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(chat_id, "Картинка сохранена")
        theme = message.json['caption']
        botDB.save_meme(filename, theme)
        bot.send_message(chat_id, "И добавлена в базу")

    except Exception as e:
        bot.send_message(chat_id, e)


@bot.message_handler(commands=['show_themes'])
def handle_show_themes(message):
    text = 'Темы мемов:\n'
    themes = botDB.get_themes_list()
    for theme in themes:
        text += f"{theme}\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.reply_to_message is not None:
        params = get_command_params(message.reply_to_message)
        if params[0] == '/add_meme':
            send_reply_photo()


def send_reply_photo(chat_id):
    markup = telebot.types.ForceReply(selective=False)
    bot.send_message(chat_id, answer_reason.ADD_FILE_TEXT, reply_markup=markup)


bot.polling()
