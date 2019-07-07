from enum import Enum

HELP_TEXT = "/meme [theme] - [theme is optional]\n" \
            "/show_themes - print all themes\n" \
            "/add_meme [category] - send file to bot and everyone could see this meme. This command is not working in " \
            "groups\n "

ADD_FILE_TEXT = "Now send me a meme as photo";

NOT_ABLE_IN_GROUP = "This command is not able in group chats\n"


class AnswerReason(Enum):
    NONE = 0
    THEME = 1
    ADD_FILE = 2
