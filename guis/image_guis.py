from guis.base_guis import GUIElement
from pygame_rendering.images import Image
from general_utils.vec2 import Vec2

class GUIImage(GUIElement):
    """A GUI element for displaying images"""
    def __init__(self, filePath: str, relativePos: Vec2 = Vec2(), visible: bool = True, rotation: float = 0.0, size: Vec2 = None):
        self.image = Image(filePath, rotation)
        super().__init__(Vec2(), relativePos, visible)
        self.setSize(size)

    def draw(self):
        self.image.blitAt(self.getAbsolutePosition())

    def setSize(self, size: Vec2):
        self.scaleTo(size)

    def getSize(self):
        return self.image.getSize()

    def scaleTo(self, size: Vec2):
        self.image.scaleTo(size)

    def scaleBy(self, scale: Vec2):
        self.image.scaleBy(scale)

    def rotateBy(self, rotation: float):
        self.image.rotateBy(rotation)

    def rotateTo(self, rotation: float):
        self.image.rotateTo(rotation)
