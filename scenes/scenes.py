from __future__ import annotations
from typing import Type
from guis.base_guis import RootContainer, GUIElement
from inspect import signature
from pygame_rendering import window

currentScene: Scene = None

class Scene:
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
    assert len(signature(sceneType.__init__).parameters) == 0 or ("self" in signature(sceneType.__init__).parameters and
                                                                  len(signature(sceneType.__init__).parameters) == 1), \
        f"Scene '{sceneType}' should have no constructor parameters (should be a pre-made scene)"
    # noinspection PyArgumentList
    switchCurrentScene(sceneType())

def stopGame():
    getCurrentScene().unload()
    window.closeWindow()

def getCurrentScene():
    assert currentScene is not None
    return currentScene
