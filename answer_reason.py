from enum import Enum

HELP_TEXT = "Привет!\n" \
            "Вот как ты можешь ко мне обращаться\n" \
            "/meme [theme] - [theme is optional]\n" \
            "/show_themes - print all themes\n"

prev = "/add_meme [category] - send file to bot and everyone could see this meme. This command is not working in " \
            "groups\n "

ADD_FILE_TEXT = "Now send me a meme as file with a theme as caption";

NOT_ABLE_IN_GROUP = "This command is not able in group chats\n"

SO_FUNNY = 'Хе-хе-хе, какая смешная картинка!\n'


class AnswerReason(Enum):
    NONE = 0
    THEME = 1
    ADD_FILE = 2
