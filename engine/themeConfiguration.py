class ThemeConfiguration:
    def __init__(self, theme):
        self.name = theme[0]
        self.creator = theme[1]
        self.bodyRGB = (theme[2], theme[3], theme[4])
        self.borderRGB = (theme[5], theme[6], theme[7])
        self.numberRGB = (theme[8], theme[9], theme[10])
        self.hourLineRGB = (theme[11], theme[12], theme[13])
        self.minLineRGB = (theme[14], theme[15], theme[16])
        self.chromaKeyRGB = (theme[17], theme[18], theme[19])
        self.thumbnail = theme[20]
