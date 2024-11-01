from __future__ import annotations
from general_utils.vec2 import Vec2
import pygame
import time

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

BACKGROUND_COLOR = 0x000000

frameCount = 0

display: pygame.Surface = None

previousLastFrameTime = 0
lastFrameTime = 0

isOpen: bool = False

def createWindow():
    """create a window and initialize pygame"""
    global display, previousLastFrameTime, lastFrameTime, isOpen
    if display is None:
        pygame.init()
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        previousLastFrameTime = time.time()
        lastFrameTime = time.time()

        isOpen = True

def refreshWindow():
    """refreshes the window

    more precisely, it updates the Pygame display (draws any images that were blitted to the screen) and
    then sets the screen to the background color so that any new images are ready to be drawn on top

    should be called exactly once every frame so that all images are displayed as intended"""
    global frameCount, previousLastFrameTime, lastFrameTime
    pygame.display.update()
    display.fill(BACKGROUND_COLOR)
    frameCount += 1
    previousLastFrameTime = lastFrameTime
    lastFrameTime = time.time()

def closeWindow():
    global isOpen
    isOpen = False

def getScreenSize():
    return Vec2(SCREEN_WIDTH, SCREEN_HEIGHT)

def getDelta():
    return lastFrameTime - previousLastFrameTime
