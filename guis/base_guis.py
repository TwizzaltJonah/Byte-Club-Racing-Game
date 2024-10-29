from __future__ import annotations
from general_utils.vec2 import Vec2
from abc import abstractmethod, ABC
from pygame_rendering import window

class GUIElement(ABC):
    """Base class for all GUI elements

    GUI elements should generally be things that stay in one place on the screen and
    do not exist in the game world (such as menu buttons, for example)

    All GUI elements (including containers) can be added to containers
    This should make a sort of tree structure with a RootContainer as the root
    """

    def __init__(self, size: Vec2 = Vec2(), relativePos: Vec2 = Vec2(0, 0), visible: bool = True):
        self.relativePos = relativePos
        self.__size = size
        self.visible = visible
        self.parent: GUIContainer | type(None) = None

    @abstractmethod
    def draw(self):
        """draw this element

        this method should be called every frame for every element that is a descendant of the RootContainer.
        this method should include anything that needs to be updated every frame, but will mostly be used for drawing things with images to the screen

        this method should not be called if 'visible' is False
        """
        pass

    def unload(self):
        """function to be called when this element is unloaded"""
        pass

    def addToContainer(self, container: GUIContainer):
        container.addChild(self)

    def onAddedToContainer(self, container: GUIContainer):
        """callback function so that inheritors can detect when they are added to a container"""
        pass

    def toggleVisible(self):
        self.visible = not self.visible

    def setSize(self, size: Vec2):
        self.__size = size

    def getSize(self):
        return self.__size

    # TODO: create an absolutePosition field that gets updated with relative
    #  positions so that this doesn't need to called every frame for every image
    # (maybe it would be better to calculate it every frame idk)
    def getAbsolutePosition(self):
        """return the absolute position of this element

        the absolute position is calculated from adding any offsets of itself or any parent containers
        """
        if self.parent is None:
            return Vec2(0, 0)
        else:
            return self.relativePos + self.parent.getChildOffset(self) + self.parent.getAbsolutePosition()


class GUIContainer(GUIElement):
    """Base class for all GUI containers

    GUI containers generally should not 'do' anything other than group their children together and change their positions
    """

    def __init__(self, size: Vec2 = Vec2(0.0, 0.0), relativePos: Vec2 = Vec2(0, 0),
                 visible: bool = True, children: list[GUIElement] = None):
        super().__init__(size, relativePos, visible)
        if children is None:
            children = []
        self._children: list[GUIElement] = children

    def draw(self):
        """call the draw method of every child that is visible"""
        super().draw()
        for child in self.getChildren():
            if child.visible:
                child.draw()

    def unload(self):
        """function to be called when this element is unloaded"""
        super().unload()
        for child in self.getChildren():
            child.unload()

    def addChild(self, child: GUIElement):
        assert child.parent is None, "Element already added to a container"

        child.parent = self
        self._children.append(child)
        child.onAddedToContainer(self)

        return self

    def getChildOffset(self, child: GUIElement):
        """return a Vec2 of a specific child's position relative to this container

        should be overridden by subclasses that modifies the position of their children individually rather
        than all together (which would be done by changing the relativePos attribute of the container)
        """
        assert child in self.getChildren(), "Element not a child of this container"
        return Vec2()

    def getChildren(self):
        return self._children

class LayeredGUIContainer(GUIContainer):

    def __init__(self, size: Vec2 = Vec2(0.0, 0.0), relativePos: Vec2 = Vec2(0, 0),
                 visible: bool = True, children: list[GUIElement] = None, childrenLayers: list[int] = None):
        super().__init__(size, relativePos, visible)

        if children is None:
            children = []
        if childrenLayers is None:
            childrenLayers = []

        assert len(children) == len(childrenLayers)

        self._children = dict()

        for i in range(len(children)):
            self.addChild(children[i], childrenLayers[i])

    def addChild(self, child: GUIElement, layer: int = 0):
        assert child.parent is None, "Element already added to a container"

        child.parent = self

        if layer in self._children.keys():
            self._children[layer].append(child)
        else:
            self._children[layer] = [child]

        child.onAddedToContainer(self)

        return self

    def getChildren(self):
        return [child for layer in sorted(self._children.keys()) for child in self._children[layer]]

class RootContainer(GUIContainer):  # not sure if this needs its own class or not, but I thought why not
    pass
