import time

import pygame
from events.event_handler import PygameEventListener, broadcastPygameEvents
from pygame_rendering import window
from guis.base_guis import RootContainer
from guis.container_guis import AlignmentContainer
from guis.image_guis import GUIImage
from general_utils.vec2 import Vec2
from pygame_rendering.images import Image
from guis.interactable_guis import ImageButton

isRunning: bool = True
rootGUI: RootContainer = None
image: GUIImage = None
testImage: Image = None

def main():
    start()
    while isRunning:
        mainLoop()
    pygame.quit()

def start():
    window.createWindow()

    quitEvent = PygameEventListener(pygame.QUIT, stopProgram)
    quitEvent.add()

    # create a gui to draw to (just to test)
    # NOTE: in the future, there will be a scene system so that you can easily switch between GUIs and also render the game world
    global rootGUI, image
    rootGUI = RootContainer()
    alignmentContainer = AlignmentContainer()

    image = GUIImage("sprites/SpriteTest.png")
    image.image.scaleBy(Vec2(40, 40))

    rootGUI.addChild(alignmentContainer)
    alignmentContainer.addChild(image, "CENTER")

    button = ImageButton("sprites/SpriteTest.png", size=Vec2(128, 128), onDown=stopProgram)
    rootGUI.addChild(button)

    rootGUI.load()


def mainLoop():
    global isRunning

    # will be replaced when scenes are added
    rootGUI.draw()

    broadcastPygameEvents(pygame.event.get())

    window.refreshWindow()

    # testing stuff
    image.image.rotateBy(window.getDelta() * 60)


def stopProgram():
    global isRunning
    isRunning = False
    rootGUI.unload()


if __name__ == '__main__':
    main()

