from __future__ import annotations
from typing import Type
from guis.base_guis import RootContainer, GUIElement
from inspect import signature
from pygame_rendering import window

currentScene: Scene = None

class Scene:
    """Scene class for handling GUIs and the game world

    Should generally be at the highest level, such that switching from one scene to
    another will have no side effects and will retain nothing from the previous scene

    Scenes do not have to have a game world, and can instead be purely GUI scenes
    such as the main menu or other menus"""
    hasGameWorld = False

    def __init__(self, guiRoot: RootContainer):
        self.guiRoot = guiRoot

    def onFrame(self):
        self.guiRoot.draw()

    def load(self):
        self.guiRoot.load()

    def unload(self):
        self.guiRoot.unload()

def switchCurrentScene(scene: Scene):
    global currentScene
    if currentScene is not None:
        currentScene.unload()
    currentScene = scene
    currentScene.load()

def switchCurrentSceneByType(sceneType: Type[Scene]):
    assert len(signature(sceneType.__init__).parameters) == 0 or ("self" in signature(sceneType.__init__).parameters and len(signature(sceneType.__init__).parameters) == 1), \
        f"Scene '{sceneType}' should have no constructor parameters (should be a pre-made scene)"
    # noinspection PyArgumentList
    switchCurrentScene(sceneType())

def stopGame():
    getCurrentScene().unload()
    window.closeWindow()

def getCurrentScene():
    assert currentScene is not None
    return currentScene
