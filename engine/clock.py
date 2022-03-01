import pygame
import pyautogui
import os
import win32api
import win32con
import win32gui
from datetime import datetime
from threading import Thread

from engine import settingsManager
from engine import themeManager
from engine import render
from engine import arm
from engine import head
from engine import menu

import aboutWindow
import configurationWindow

pygame.init()
pygame.font.init()


class Clock(object):
    def __init__(self, window: pygame.Surface, windowInfo: dict):
        self.window = window
        self.windowInfo = windowInfo
        self.oldBorderlessOption = None
        self.hwnd = pygame.display.get_wm_info()["window"]

        self.windowIcon = pygame.image.load(os.path.join("image", "icon", "icon.png"))
        self.clock = pygame.time.Clock()
        self.running = True
        self.clockRender = render.Clock(numberFont=self.Fonts.clockNumberFont)

        self.windowMoving = False
        self.windowMousePos = [0, 0]

        self.windowOpen = False
        self.menuOpen = False

        self.windowThread = None

        self.update_head_pos = pygame.USEREVENT + 1
        pygame.time.set_timer(self.update_head_pos, 1000)

        self.settingsManager = settingsManager.Settings()
        self.settings = self.settingsManager.get_settings()
        self.themes = themeManager.ThemeManager()
        self.currentTheme = self.themes.get_all_themes()["{}".format(self.settings.theme)]
        if self.settings is None:
            print("Default settings used due to error loading main settings file")
            self.settings = self.settingsManager.get_backup()

        self.windowX = self.settings.winSize
        self.windowY = self.settings.winSize

        self.arms = arm.Arm(window=self.window, settings=self.settings, images=self.Images,
                            windowX=self.windowX, windowY=self.windowY)
        self.head = head.Head(window=self.window, settings=self.settings, images=self.Images,
                              windowX=self.windowX, windowY=self.windowY)

        self.menu = menu.Menu(window=self.window, settings=self.settings)

        self.christmasDays = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                              "21", "22", "23", "24", "25"]

        if self.settings.noMustacheMode:
            self.Images.head = pygame.image.load(os.path.join("image", "mumbo", "headNoMustache.png")).convert_alpha()
            self.Images.headSleep = pygame.image.load(os.path.join("image", "mumbo", "headSleepNoMustache.png")).convert_alpha()
            self.Images.headBDay = pygame.image.load(os.path.join("image", "birthday", "headNoMustache.png")).convert_alpha()
            self.Images.headSleepBDay = pygame.image.load(os.path.join("image", "birthday", "headSleepNoMustache.png")).convert_alpha()
            self.Images.xmasHead = pygame.image.load(os.path.join("image", "christmas", "headNoMustache.png")).convert_alpha()
            self.Images.xmasHeadSleep = pygame.image.load(os.path.join("image", "christmas", "headSleepNoMustache.png")).convert_alpha()
        if self.settings.grianMode:
            self.Images.body = pygame.image.load(os.path.join("image", "grian", "body.png")).convert_alpha()
            self.Images.tie = pygame.image.load(os.path.join("image", "grian", "tie.png")).convert_alpha()
            self.Images.head = pygame.image.load(os.path.join("image", "grian", "head.png")).convert_alpha()
            self.Images.headSleep = pygame.image.load(os.path.join("image", "grian", "headSleep.png")).convert_alpha()
            self.Images.longHand = pygame.image.load(os.path.join("image", "grian", "longHand.png")).convert_alpha()
            self.Images.shortHand = pygame.image.load(os.path.join("image", "grian", "shortHand.png")).convert_alpha()
            self.Images.longHandSpoon = pygame.image.load(os.path.join("image", "grian", "longHandSpoon.png")).convert_alpha()
            self.Images.shortHandSpoon = pygame.image.load(os.path.join("image", "grian", "shortHandSpoon.png")).convert_alpha()
            self.Images.headBDay = pygame.image.load(os.path.join("image", "birthday", "headGrian.png")).convert_alpha()
            self.Images.headSleepBDay = pygame.image.load(os.path.join("image", "birthday", "headSleepGrian.png")).convert_alpha()

            self.Images.xmasTie = pygame.image.load(os.path.join("image", "christmas", "grianTie.png")).convert_alpha()
            self.Images.xmasHead = pygame.image.load(os.path.join("image", "christmas", "grianHead.png")).convert_alpha()
            self.Images.xmasHeadSleep = pygame.image.load(os.path.join("image", "christmas", "grianHeadSleep.png")).convert_alpha()
            self.Images.xmasLongHandSpoon = pygame.image.load(os.path.join("image", "christmas", "grianLongHandSpoon.png")).convert_alpha()
            self.Images.xmasShortHandSpoon = pygame.image.load(os.path.join("image", "christmas", "grianShortHandSpoon.png")).convert_alpha()

    class Images:
        body = pygame.image.load(os.path.join("image", "mumbo", "body.png")).convert_alpha()
        tie = pygame.image.load(os.path.join("image", "mumbo", "tie.png")).convert_alpha()
        head = pygame.image.load(os.path.join("image", "mumbo", "head.png")).convert_alpha()
        headSleep = pygame.image.load(os.path.join("image", "mumbo", "headSleep.png")).convert_alpha()
        longHand = pygame.image.load(os.path.join("image", "mumbo", "longHand.png")).convert_alpha()
        shortHand = pygame.image.load(os.path.join("image", "mumbo", "shortHand.png")).convert_alpha()
        longHandSpoon = pygame.image.load(os.path.join("image", "mumbo", "longHandSpoon.png")).convert_alpha()
        shortHandSpoon = pygame.image.load(os.path.join("image", "mumbo", "shortHandSpoon.png")).convert_alpha()

        headBDay = pygame.image.load(os.path.join("image", "birthday", "head.png")).convert_alpha()
        headSleepBDay = pygame.image.load(os.path.join("image", "birthday", "headSleep.png")).convert_alpha()

        xmasBody = pygame.image.load(os.path.join("image", "christmas", "body.png")).convert_alpha()
        xmasTie = pygame.image.load(os.path.join("image", "christmas", "tie.png")).convert_alpha()
        xmasHead = pygame.image.load(os.path.join("image", "christmas", "head.png")).convert_alpha()
        xmasHeadSleep = pygame.image.load(os.path.join("image", "christmas", "headSleep.png")).convert_alpha()
        xmasLongHand = pygame.image.load(os.path.join("image", "christmas", "longHand.png")).convert_alpha()
        xmasShortHand = pygame.image.load(os.path.join("image", "christmas", "shortHand.png")).convert_alpha()
        xmasLongHandSpoon = pygame.image.load(os.path.join("image", "christmas", "longHandSpoon.png")).convert_alpha()
        xmasShortHandSpoon = pygame.image.load(os.path.join("image", "christmas", "shortHandSpoon.png")).convert_alpha()

    class Fonts:
        clockNumberFont = pygame.font.Font(os.path.join("font", "RifficFree.ttf"), 24)
        FPSFont = pygame.font.Font(os.path.join("font", "bebasRegular.ttf"), 20)

    def update_window_props(self):
        self.windowX = self.settings.winSize
        self.windowY = self.settings.winSize
        
        if self.oldBorderlessOption != self.settings.borderlessWin:
            if not self.settings.borderlessWin:
                pygame.display.set_mode([self.windowX, self.windowY], 0, 32, pygame.DOUBLEBUF)
                pygame.display.set_icon(self.windowIcon)
            else:
                pygame.display.set_mode([self.windowX, self.windowY], pygame.NOFRAME)
            self.oldBorderlessOption = self.settings.borderlessWin

    def move_window(self):
        mousePos = pyautogui.position()
        windowRelativeX = mousePos[0] - self.windowMousePos[0]
        windowRelativeY = mousePos[1] - self.windowMousePos[1]

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowRelativeX, windowRelativeY)

    def update_window_pos(self):
        if not self.settings.borderlessWin:
            pygame.display.set_mode((self.windowX, self.windowY + 1), 0, 32, pygame.DOUBLEBUF)
            pygame.display.set_mode((self.windowX, self.windowY), 0, 32, pygame.DOUBLEBUF)
            pygame.display.set_icon(self.windowIcon)
        else:
            pygame.display.set_mode((self.windowX, self.windowY + 1), pygame.NOFRAME)
            pygame.display.set_mode((self.windowX, self.windowY), pygame.NOFRAME)

    def update_chroma_key(self):
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*self.currentTheme.chromaKeyRGB),
                                            0, win32con.LWA_COLORKEY)

    def check_xmas_mode(self):
        if self.settings.xmasMode:
            date_time = datetime.today()

            if str(date_time.month) == "12" and str(date_time.day) in self.christmasDays:
                return True
        return False

    def draw(self):
        self.window.fill(self.currentTheme.chromaKeyRGB)

        pygame.draw.circle(self.window, self.currentTheme.bodyRGB, [int(self.windowX / 2), int(self.windowY / 2)],
                           int(self.windowX / 2))

        self.window.blit(pygame.transform.smoothscale(self.clockRender.clock_render, [self.windowX, self.windowY]),
                         [0, 0])

        if self.check_xmas_mode():
            self.window.blit(pygame.transform.smoothscale(self.Images.xmasBody, [self.windowX, self.windowY]), [0, 0])
        else:
            self.window.blit(pygame.transform.smoothscale(self.Images.body, [self.windowX, self.windowY]), [0, 0])

        self.arms.draw()

        if self.check_xmas_mode():
            self.window.blit(pygame.transform.smoothscale(self.Images.xmasTie, [self.windowX, self.windowY]), [0, 0])
        else:
            self.window.blit(pygame.transform.smoothscale(self.Images.tie, [self.windowX, self.windowY]), [0, 0])

        self.head.draw()

        if self.menuOpen:
            self.menu.draw()

        if self.settings.showFPS:
            self.window.blit(self.Fonts.FPSFont.render("{} FPS".format(round(self.clock.get_fps())), False,
                                                       (20, 20, 20)), [10, 10])

        pygame.display.update()

    def run(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 10)
        self.update_window_props()

        if self.settings.enableChroma:
            self.update_chroma_key()

        self.clockRender.render(theme=self.currentTheme,
                                settings=self.settings)

        while self.running:
            self.update_window_props()

            self.clock.tick(self.settings.FPSLimit)

            self.arms.update_hand_rotation()
            self.head.update_visual_position()

            if self.menuOpen:
                self.menu.update(mouse_position=pygame.mouse.get_pos(), mouse_button_clicked=pygame.mouse.get_pressed())

            self.draw()

            if self.windowThread is not None:
                if not self.windowThread.is_alive():
                    self.windowThread = None
                    self.windowOpen = False

            if not self.menuOpen:
                mousePressedInfo = pygame.mouse.get_pressed()
                if mousePressedInfo[0] == 1 and not self.windowMoving:
                    self.windowMoving = True
                    self.windowMousePos = pygame.mouse.get_pos()
                    self.move_window()
                if mousePressedInfo[0] == 1 and self.windowMoving:
                    self.move_window()
                if mousePressedInfo[0] == 0 and self.windowMoving:
                    self.windowMoving = False
                    self.update_window_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.update_head_pos:
                    self.head.update_position()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.menuOpen:
                        if event.button == 1:
                            next_event = self.menu.check_clicked(mouse_position=event.pos)

                            if next_event == 0:
                                if not self.windowOpen:
                                    self.windowOpen = True
                                    self.windowThread = Thread(target=aboutWindow.open_window)
                                    self.windowThread.start()
                            elif next_event == 1:
                                if not self.windowOpen:
                                    self.windowOpen = True
                                    self.windowThread = Thread(target=configurationWindow.open_window)
                                    self.windowThread.start()
                            elif next_event == 2:
                                self.running = False

                    if event.button == 3:
                        if not self.menuOpen:
                            self.menuOpen = True
                        else:
                            self.menuOpen = False
                    else:
                        self.menuOpen = False
