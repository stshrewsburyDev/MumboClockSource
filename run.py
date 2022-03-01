import pygame
import sys

if __name__ == "__main__":
    windowInfo = {"windowName": "Mumbo clock",
                  "defaultX": 771,
                  "defaultY": 771}

    pygame.init()

    window = pygame.display.set_mode((windowInfo["defaultX"], windowInfo["defaultY"]), pygame.NOFRAME)
    pygame.display.set_caption(windowInfo["windowName"])

    from engine.clock import Clock

    mumboClock = Clock(window=window, windowInfo=windowInfo)
    mumboClock.run()

    pygame.quit()

    sys.exit()
