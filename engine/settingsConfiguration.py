class SettingsConfiguration:
    def __init__(self, settings):
        self.winSize = settings["winSize"]
        self.showFPS = settings["showFPS"]
        self.FPSLimit = settings["FPSLimit"]
        self.borderlessWin = settings["borderlessWin"]
        self.enableChroma = settings["enableChroma"]
        self.theme = settings["theme"]
        self.showAnimations = settings["showAnimations"]
        self.showNumbers = settings["showNumbers"]
        self.showHourLines = settings["showHourLines"]
        self.showMinLines = settings["showMinLines"]
        self.showBorder = settings["showBorder"]
        self.nightModeActive = settings["nightModeActive"]
        self.spoonHoursActive = settings["spoonHoursModeActive"]
        self.noMustacheMode = settings["noMustacheMode"]
        self.grianMode = settings["grianMode"]
        self.birthdayMode = settings["seasonalModes"]["birthday"]
        self.xmasMode = settings["seasonalModes"]["xmas"]

    def convert_to_json(self):
        return {"winSize": self.winSize,
                "showFPS": self.showFPS,
                "FPSLimit": self.FPSLimit,
                "borderlessWin": self.borderlessWin,
                "enableChroma": self.enableChroma,
                "theme": self.theme,
                "showAnimations": self.showAnimations,
                "showNumbers": self.showNumbers,
                "showHourLines": self.showHourLines,
                "showMinLines": self.showMinLines,
                "showBorder": self.showBorder,
                "nightModeActive": self.nightModeActive,
                "spoonHoursModeActive": self.spoonHoursActive,
                "noMustacheMode": self.noMustacheMode,
                "grianMode": self.grianMode,
                "seasonalModes": {
                    "birthday": self.birthdayMode,
                    "xmas": self.xmasMode
                }}

