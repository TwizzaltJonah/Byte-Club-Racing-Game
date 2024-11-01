from guis.base_guis import GUIElement, GUIContainer
from guis.image_guis import GUIImage
from pygame_rendering.images import Image
from general_utils.vec2 import Vec2
from general_utils.rect import Rect
from events.event_handler import PygameEventListener
import pygame

class Button(GUIElement):

    def __init__(self, size: Vec2 = Vec2(), relativePos: Vec2 = Vec2(), onDown: callable = None, onDownArgs: tuple = (), onUp: callable = None, onUpArgs: tuple = ()):
        super().__init__(size, relativePos)

        self.onDown = onDown
        self.onDownArgs = onDownArgs

        self.onUp = onUp
        self.onUpArgs = onUpArgs

        self.onDownEventListener = PygameEventListener(pygame.MOUSEBUTTONDOWN, self.onMouseDown, True)
        self.onUpEventListener = PygameEventListener(pygame.MOUSEBUTTONUP, self.onMouseUp, True)

    def load(self):
        super().load()
        self.onDownEventListener.add()
        self.onUpEventListener.add()

    def unload(self):
        super().unload()
        self.onDownEventListener.remove()
        self.onUpEventListener.remove()

    def onMouseDown(self, event: pygame.event.EventType):
        if self.onDown is not None and Rect(self.getAbsolutePosition(), self.getSize()).isPointInside(Vec2.fromTuple(event.dict["pos"])):
            self.onDown(*self.onDownArgs)

    def onMouseUp(self, event: pygame.event.EventType):
        if self.onUp is not None and Rect(self.getAbsolutePosition(), self.getSize()).isPointInside(Vec2.fromTuple(event.dict["pos"])):
            self.onUp(*self.onUpArgs)

    def draw(self):
        pass

class ImageButton(Button):

    def __init__(self, filePath: str, relativePos: Vec2 = Vec2(), visible: bool = True, rotation: float = 0.0, size: Vec2 = None,
                 onDown: callable = None, onDownArgs: tuple = (), onUp: callable = None, onUpArgs: tuple = ()):
        self.image = Image(filePath, rotation, size)
        self.visible = visible
        super().__init__(self.image.getSize(), relativePos, onDown, onDownArgs, onUp, onUpArgs)

    def draw(self):
        super().draw()
        self.image.blitAt(self.getAbsolutePosition())

    def unload(self):
        super().unload()
        self.onDownEventListener.remove()
        self.onUpEventListener.remove()

    def setSize(self, size: Vec2):
        self.image.scaleTo(size)

    def getSize(self):
        return self.image.getSize()
