import mysql.connector
import mysql.connector.cursor


class TeeBotDB:
    DB = None
    Cursor = None

    def __init__(self):
        self.DB = mysql.connector.connect(
            host='116.203.77.112',
            user='teenik',
            passwd='33153315',
            database='TeeBotDB'
        )
        self.Cursor = self.DB.cursor()

    def get_themes_list(self):
        self.Cursor.execute('select distinct theme from memes')
        themes = [item[0] for item in self.Cursor.fetchall()]
        return themes

    def get_random_meme(self):
        self.Cursor.execute("select filename FROM memes ORDER BY RAND() LIMIT 1;")
        return self.Cursor.fetchall()[0][0]

    def get_meme_by_theme(self, theme):
        self.Cursor.execute(f"select filename FROM memes WHERE theme = '{theme}' ORDER BY RAND() LIMIT 1;")
        return self.Cursor.fetchall()[0][0]

