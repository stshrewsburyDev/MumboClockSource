import pygame
from datetime import datetime

from engine import settingsConfiguration


class Arm:
    def __init__(self, window: pygame.Surface, settings: settingsConfiguration.SettingsConfiguration, images,
                 windowX: int, windowY: int):
        self.window = window
        self.settings = settings
        self.images = images
        self.windowX = windowX
        self.windowY = windowY

        self.rotationMin = 0
        self.visualRotationMin = 0
        self.rotationHour = 0
        self.visualRotationHour = 0

        self.christmasDays = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                              "21", "22", "23", "24", "25"]

    def check_spoon_mode(self):
        if not self.settings.spoonHoursActive:
            return False

        date_time = datetime.now()
        hour = date_time.hour

        if hour == 12 or hour == 13:
            return True
        return False

    def check_xmas_mode(self):
        if self.settings.xmasMode:
            date_time = datetime.today()

            if str(date_time.month) == "12" and str(date_time.day) in self.christmasDays:
                return True
        return False

    def update_hand_rotation(self):
        date_time = datetime.now()
        hour = date_time.hour
        minute = date_time.minute
        second = date_time.second

        if hour != 0:
            if hour == 24:
                hour = 0
            elif hour >= 12:
                hour -= 12
        if minute == 60:
            minute = 0
        if second == 60:
            second = 0

        self.rotationHour = ((360 / 12) * hour) + ((360 / 12 / 60) * minute)
        self.rotationMin = ((360 / 60) * minute) + ((360 / 60 / 60) * second)

        self.update_visual_hand_rotation()

    def update_visual_hand_rotation(self):
        if not self.settings.showAnimations:
            self.visualRotationMin = self.rotationMin
            self.visualRotationHour = self.rotationHour
        else:
            if self.rotationMin == 0:
                self.visualRotationMin = 0
            else:
                self.visualRotationMin += (self.rotationMin - self.visualRotationMin) / 50

            if self.rotationHour == 0:
                self.visualRotationHour = 0
            else:
                self.visualRotationHour += (self.rotationHour - self.visualRotationHour) / 50

    @staticmethod
    def rotate_blit(surface: pygame.Surface, image: pygame.Surface, angle):
        rect = image.get_rect()

        rotatedImage = pygame.transform.rotozoom(image, angle, 1)

        imageX, imageY = rect.center
        rect = rotatedImage.get_rect()
        rect.center = (imageX, imageY)

        surface.blit(rotatedImage, rect)

    def draw(self):
        xmasMode = self.check_xmas_mode()
        spoonMode = self.check_spoon_mode()

        if xmasMode:
            if spoonMode:
                self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.xmasLongHandSpoon,
                                                                                         [self.windowX, self.windowY]),
                                 angle=-self.visualRotationMin)
                self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.xmasShortHandSpoon,
                                                                                         [self.windowX, self.windowY]),
                                 angle=-self.visualRotationHour)
            else:
                self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.xmasLongHand,
                                                                                         [self.windowX, self.windowY]),
                                 angle=-self.visualRotationMin)
                self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.xmasShortHand,
                                                                                         [self.windowX, self.windowY]),
                                 angle=-self.visualRotationHour)
        elif spoonMode:
            self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.longHandSpoon,
                                                                                     [self.windowX, self.windowY]),
                             angle=-self.visualRotationMin)
            self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.shortHandSpoon,
                                                                                     [self.windowX, self.windowY]),
                             angle=-self.visualRotationHour)
        else:
            self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.longHand,
                                                                                     [self.windowX, self.windowY]),
                             angle=-self.visualRotationMin)
            self.rotate_blit(surface=self.window, image=pygame.transform.smoothscale(self.images.shortHand,
                                                                                     [self.windowX, self.windowY]),
                             angle=-self.visualRotationHour)
