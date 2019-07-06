from enum import Enum

HELP_TEXT = "/meme [theme] - show meme by theme[theme is optional]\n" \
       "/show_themes - print all themes\n" \
       "/add_meme [category] - send file to bot and everyone could see this meme\n"

class AnswerReason(Enum):
    NONE = 0
    THEME = 1
    ADD_FILE = 2
