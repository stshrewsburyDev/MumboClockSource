import pygame
from pygame import gfxdraw
import os

from engine import themeConfiguration
from engine import settingsConfiguration

pygame.init()
pygame.font.init()


class Clock:
    def __init__(self, numberFont):
        self.clock_render = pygame.Surface((771, 771), pygame.SRCALPHA)
        self.clock_render.convert_alpha()

        self.numberFont = numberFont

        self.hourLines = [[(382, 71),  90],
                          [(517, 112), 60],
                          [(618, 225), 30],
                          [(656, 382), 0],
                          [(619, 518), 330],
                          [(518, 619), 300],
                          [(382, 656), 270],
                          [(225, 620), 240],
                          [(112, 519), 210],
                          [(70, 382),  180],
                          [(112, 225), 150],
                          [(225, 112), 120]]
        self.minLines = [[(414, 74), 84], [(444, 79), 78], [(474, 88), 72], [(503, 99), 66],
                         [(556, 131), 54], [(580, 152), 48], [(602, 175), 42], [(622, 200), 36],
                         [(653, 256), 24], [(664, 287), 18], [(671, 318), 12], [(676, 350), 6],
                         [(676, 414), 354], [(671, 444), 348], [(664, 474), 342], [(653, 503), 336],
                         [(622, 556), 324], [(602, 580), 318], [(580, 602), 312], [(556, 622), 306],
                         [(503, 653), 294], [(474, 664), 288], [(444, 672), 282], [(414, 676), 276],
                         [(351, 676), 264], [(318, 672), 258], [(287, 664), 252], [(256, 653), 246],
                         [(200, 622), 234], [(175, 602), 228], [(152, 580), 222], [(131, 556), 216],
                         [(99, 503), 204], [(88, 474), 198], [(79, 444), 192], [(74, 414), 186],
                         [(74, 350), 174], [(79, 318), 168], [(87, 287), 162], [(99, 256), 156],
                         [(131, 200), 144], [(152, 175), 138], [(175, 152), 132], [(200, 131), 126],
                         [(256, 99), 114], [(287, 88), 108], [(318, 79), 102], [(350, 74), 96]]
        self.numbers = [["12", [374, 36]],
                        ["1", [544, 85]],
                        ["2", [668, 206]],
                        ["3", [714, 370]],
                        ["4", [668, 536]],
                        ["5", [546, 660]],
                        ["6", [380, 704]],
                        ["7", [214, 660]],
                        ["8", [94, 536]],
                        ["9", [46, 370]],
                        ["10", [88, 204]],
                        ["11", [212, 85]]]

    def clear(self):
        self.clock_render.fill((255, 255, 255, 0))

    @staticmethod
    def draw_h_line(colour):
        line = pygame.Surface([46, 7], pygame.SRCALPHA, 32)
        line.convert_alpha()

        end_render = pygame.Surface([15, 15], pygame.SRCALPHA, 32)
        gfxdraw.filled_circle(end_render, 7, 7, 7, colour)
        gfxdraw.aacircle(end_render, 7, 7, 7, colour)
        end_render = pygame.transform.smoothscale(end_render, [7, 7])

        line.blit(end_render, [0, 0])
        line.blit(end_render, [39, 0])
        pygame.draw.rect(line, colour, pygame.Rect(3, 0, 40, 7))

        return line

    @staticmethod
    def draw_m_line(colour):
        line = pygame.Surface([24, 5], pygame.SRCALPHA, 32)
        line.convert_alpha()

        end_render = pygame.Surface([11, 11], pygame.SRCALPHA, 32)
        gfxdraw.filled_circle(end_render, 5, 5, 5, colour)
        gfxdraw.aacircle(end_render, 5, 5, 5, colour)
        end_render = pygame.transform.smoothscale(end_render, [5, 5])
        
        line.blit(end_render, [0, 0])
        line.blit(end_render, [19, 0])
        pygame.draw.rect(line, colour, pygame.Rect(2, 0, 20, 5))

        return line

    def render(self, theme: themeConfiguration.ThemeConfiguration,
               settings: settingsConfiguration.SettingsConfiguration):
        self.clear()

        if settings.showBorder:
            border = pygame.Surface([1542, 1542], pygame.SRCALPHA, 32)
            pygame.draw.circle(border, theme.borderRGB, [770, 770], 746, 40)
            self.clock_render.blit(pygame.transform.smoothscale(border, [771, 771]), [0, 0])

        if settings.showHourLines:
            for line in self.hourLines:
                self.clock_render.blit(pygame.transform.rotozoom(self.draw_h_line(theme.hourLineRGB),
                                                                 line[1], 1), line[0])

            if settings.showMinLines:
                for line in self.minLines:
                    self.clock_render.blit(pygame.transform.rotozoom(self.draw_m_line(colour=theme.minLineRGB),
                                                                     line[1], 1), line[0])

        if settings.showNumbers:
            for number in self.numbers:
                render = self.numberFont.render("{}".format(number[0]), True, theme.numberRGB)
                self.clock_render.blit(render, number[1])
