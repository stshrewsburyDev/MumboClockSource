import json
import os

from engine import settingsConfiguration


class Settings:
    def __init__(self):
        self.path = os.path.join("config", "settings.json")
        self.defaultSettings = {"winSize": 250,
                                "showFPS": 0,
                                "FPSLimit": 30,
                                "borderlessWin": 1,
                                "enableChroma": 1,
                                "theme": "Default",
                                "showAnimations": 0,
                                "showNumbers": 1,
                                "showHourLines": 1,
                                "showMinLines": 1,
                                "showBorder": 1,
                                "nightModeActive": 0,
                                "spoonHoursModeActive": 0,
                                "noMustacheMode": 0,
                                "grianMode": 0,
                                "seasonalModes": {
                                    "birthday": 0,
                                    "xmas": 0
                                }}

    def get_settings(self):
        try:
            with open(self.path, "r") as settingsFile:
                return settingsConfiguration.SettingsConfiguration(json.load(settingsFile))
        except Exception as error:
            print("Exception at engine.settingsManager.Settings.get_settings(): {0}".format(error))
            return None

    def save_settings(self, settings):
        try:
            with open(self.path, "w") as settingsFile:
                json.dump(settings, settingsFile)
                return True
        except Exception as error:
            print("Exception at engine.settingsManager.Settings.save_settings(): {0}".format(error))
            return False

    def get_backup(self):
        return settingsConfiguration.SettingsConfiguration(self.defaultSettings)
