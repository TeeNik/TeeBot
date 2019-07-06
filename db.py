import mysql.connector


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
        self.Cursor = DB.Cursor()

    def get_themes_list(self):
        self.Cursor.execute('select distinct theme from memes')
        return self.Cursor.fetchall()
