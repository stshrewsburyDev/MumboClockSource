import pygame
from datetime import datetime

from engine import settingsConfiguration


class Head:
    def __init__(self, window: pygame.Surface, settings: settingsConfiguration.SettingsConfiguration, images,
                 windowX: int, windowY: int):
        self.window = window
        self.settings = settings
        self.images = images
        self.windowX = windowX
        self.windowY = windowY

        self.rotation = 5
        self.visualRotation = 0
        self.Y = 0
        self.visualY = 0

        self.christmasDays = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                              "21", "22", "23", "24", "25"]

    def check_night_mode(self):
        if self.settings.nightModeActive:
            date_time = datetime.now()
            hour = date_time.hour

            if hour >= 22 or hour <= 8:
                return True
        return False

    def check_birthday_mode(self):
        if self.settings.birthdayMode:
            date_time = datetime.today()

            if str(date_time.month) == "12" and str(date_time.day) == "1":
                return True
        return False

    def check_xmas_mode(self):
        if self.settings.xmasMode:
            date_time = datetime.today()

            if str(date_time.month) == "12" and str(date_time.day) in self.christmasDays:
                return True
        return False

    def update_position(self):
        if self.check_night_mode():
            self.rotation = 5
            if self.Y == -2:
                self.Y = 2
            else:
                self.Y = -2
        else:
            if self.rotation == -10:
                self.rotation = 10
            else:
                self.rotation = -10

    def update_visual_position(self):
        self.visualRotation += (self.rotation - self.visualRotation) / 40
        self.visualY += (self.Y - self.visualY) / 10

    @staticmethod
    def rotate_blit(surface: pygame.Surface, image: pygame.Surface, angle, y_offset):
        rect = image.get_rect()

        rotatedImage = pygame.transform.rotozoom(image, angle, 1)

        imageX, imageY = rect.center
        rect = rotatedImage.get_rect()
        rect.center = (imageX, imageY + y_offset)

        surface.blit(rotatedImage, rect)

    def draw(self):
        nightMode = self.check_night_mode()
        birthdayMode = self.check_birthday_mode()
        xmasMode = self.check_xmas_mode()

        headImage = self.images.head
        if nightMode:
            if birthdayMode:
                headImage = self.images.headSleepBDay
            elif xmasMode:
                headImage = self.images.xmasHeadSleep
            else:
                headImage = self.images.headSleep
        elif birthdayMode:
            headImage = self.images.headBDay
        elif xmasMode:
            headImage = self.images.xmasHead

        if self.settings.showAnimations:
            self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(headImage,
                                                                                     [self.windowX, self.windowY]),
                             angle=-self.visualRotation, y_offset=self.visualY)
        else:
            self.window.blit(pygame.transform.smoothscale(headImage, [self.windowX, self.windowY]), [0, 0])
