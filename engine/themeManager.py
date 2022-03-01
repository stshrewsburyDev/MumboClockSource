import os
import sqlite3

from engine import themeConfiguration


class ThemeManager:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join("config", "themes.db"))
        self.cursor = self.connection.cursor()

    def get_all_themes(self):
        themeList = {}

        self.cursor.execute("SELECT * FROM themes")

        themes = self.cursor.fetchall()

        for theme in themes:
            try:
                themeList["{}".format(theme[0])] = themeConfiguration.ThemeConfiguration(theme)
            except Exception as error:
                print("Exception as engine.themeManager.get_all_themes(): {0}".format(error))

        return themeList

    def get_all_themes_list(self):
        themeList = []

        self.cursor.execute("SELECT * FROM themes")

        themes = self.cursor.fetchall()

        for theme in themes:
            try:
                themeList.append(themeConfiguration.ThemeConfiguration(theme))
            except Exception as error:
                print("Exception as engine.themeManager.get_all_themes(): {0}".format(error))

        return themeList

    def close_connection(self):
        self.connection.close()
