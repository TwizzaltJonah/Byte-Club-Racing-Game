import pygame
from events.event_handler import PygameEventListener, broadcastPygameEvents
from pygame_rendering import window
from guis.base_guis import RootContainer
from guis.image_guis import GUIImage
from pygame_rendering.images import Image
from scenes.scenes import stopGame, switchCurrentScene, getCurrentScene
from scenes.gui_scenes import MainMenuScene

rootGUI: RootContainer = None
image: GUIImage = None
testImage: Image = None

def main():
    start()
    while window.isOpen:
        mainLoop()
    pygame.quit()

def start():
    window.createWindow()

    quitEvent = PygameEventListener(pygame.QUIT, stopGame)
    quitEvent.add()

    switchCurrentScene(MainMenuScene())

def mainLoop():

    getCurrentScene().onFrame()

    broadcastPygameEvents(pygame.event.get())

    window.refreshWindow()


if __name__ == '__main__':
    main()
