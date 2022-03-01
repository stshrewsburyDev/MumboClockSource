import pygame
import os

from engine import button
from engine import settingsConfiguration


class Menu:
    def __init__(self, window: pygame.Surface, settings: settingsConfiguration.SettingsConfiguration):
        self.window = window
        self.settings = settings

        self.menuSize = int(self.settings.winSize - 50)
        self.scaleSize = (100 / 730) * self.menuSize
        self.button_sizeX = int((600 / 100) * self.scaleSize)
        self.button_sizeY = int((98 / 100) * self.scaleSize)
        self.button_X = 25 + int((65 / 100) * self.scaleSize)

        self.about_button = button.Button(window=self.window, settings=self.settings,
                                          normal_img=self.Images.about_normal, hovered_img=self.Images.about_hovered,
                                          clicked_img=self.Images.about_clicked, X=self.button_X,
                                          Y=int(25 + ((160 / 100) * self.scaleSize)),
                                          sizeX=self.button_sizeX, sizeY=self.button_sizeY)
        self.settings_button = button.Button(window=self.window, settings=self.settings,
                                             normal_img=self.Images.settings_normal,
                                             hovered_img=self.Images.settings_hovered,
                                             clicked_img=self.Images.settings_clicked, X=self.button_X,
                                             Y=int(25 + ((285 / 100) * self.scaleSize)),
                                             sizeX=self.button_sizeX, sizeY=self.button_sizeY)
        self.close_button = button.Button(window=self.window, settings=self.settings,
                                          normal_img=self.Images.close_normal,
                                          hovered_img=self.Images.close_hovered,
                                          clicked_img=self.Images.close_clicked, X=self.button_X,
                                          Y=int(25 + ((410 / 100) * self.scaleSize)),
                                          sizeX=self.button_sizeX, sizeY=self.button_sizeY)

    class Images:
        menuBG = pygame.image.load(os.path.join("image", "GUI", "menu_background.png"))

        # About button
        about_normal = pygame.image.load(os.path.join("image", "GUI", "buttons", "about", "normal.png"))
        about_hovered = pygame.image.load(os.path.join("image", "GUI", "buttons", "about", "hovered.png"))
        about_clicked = pygame.image.load(os.path.join("image", "GUI", "buttons", "about", "clicked.png"))

        # Close button
        close_normal = pygame.image.load(os.path.join("image", "GUI", "buttons", "close", "normal.png"))
        close_hovered = pygame.image.load(os.path.join("image", "GUI", "buttons", "close", "hovered.png"))
        close_clicked = pygame.image.load(os.path.join("image", "GUI", "buttons", "close", "clicked.png"))

        # Settings button
        settings_normal = pygame.image.load(os.path.join("image", "GUI", "buttons", "settings", "normal.png"))
        settings_hovered = pygame.image.load(os.path.join("image", "GUI", "buttons", "settings", "hovered.png"))
        settings_clicked = pygame.image.load(os.path.join("image", "GUI", "buttons", "settings", "clicked.png"))

    def check_clicked(self, mouse_position):
        if self.about_button.mouse_over(mouse_position=mouse_position):
            return 0
        if self.settings_button.mouse_over(mouse_position=mouse_position):
            return 1
        if self.close_button.mouse_over(mouse_position=mouse_position):
            return 2

    def update(self, mouse_position, mouse_button_clicked):
        mouse_pressed = mouse_button_clicked[0]

        self.about_button.update(mouse_position=mouse_position, mouse_pressed=mouse_pressed)
        self.settings_button.update(mouse_position=mouse_position, mouse_pressed=mouse_pressed)
        self.close_button.update(mouse_position=mouse_position, mouse_pressed=mouse_pressed)

    def draw(self):
        self.window.blit(pygame.transform.smoothscale(self.Images.menuBG, [self.menuSize, self.menuSize]), [25, 25])

        self.about_button.draw()
        self.settings_button.draw()
        self.close_button.draw()
