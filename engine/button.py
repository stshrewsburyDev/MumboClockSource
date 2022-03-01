import pygame

from engine import settingsConfiguration


class Button:
    def __init__(self, window: pygame.Surface, settings: settingsConfiguration.SettingsConfiguration,
                 normal_img: pygame.Surface, hovered_img: pygame.Surface, clicked_img: pygame.Surface,
                 X: int, Y: int, sizeX: int, sizeY: int):
        self.window = window
        self.settings = settings

        self.X = X
        self.Y = Y

        self.normal_img = pygame.transform.smoothscale(normal_img, [sizeX, sizeY])
        self.hovered_img = pygame.transform.smoothscale(hovered_img, [sizeX, sizeY])
        self.clicked_img = pygame.transform.smoothscale(clicked_img, [sizeX, sizeY])

        self.current_img = self.normal_img

        self.rect = self.current_img.get_rect()
        self.rect = self.rect.move(self.X, self.Y)

    def mouse_over(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            return True
        return False

    def update(self, mouse_position, mouse_pressed):
        if self.rect.collidepoint(mouse_position):
            if mouse_pressed:
                self.current_img = self.clicked_img
            else:
                self.current_img = self.hovered_img
        else:
            self.current_img = self.normal_img

    def draw(self):
        self.window.blit(self.current_img, [self.X, self.Y])
