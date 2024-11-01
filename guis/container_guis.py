from guis.base_guis import GUIContainer, GUIElement
from general_utils.vec2 import Vec2
from pygame_rendering import window

VALID_ALIGNMENTS = ("TOP_LEFT", "TOP", "TOP_RIGHT", "LEFT", "CENTER", "RIGHT", "BOTTOM_LEFT", "BOTTOM", "BOTTOM_RIGHT")
ALIGNMENT_SHORTHANDS = ("TL", "T", "TR", "L", "C", "R", "BL", "B", "BR")

class AlignmentContainer(GUIContainer):
    """Alignment Container to align child elements to corners, faces, or the center of this container

    Will align the edge of the element to the edge of this container
    (for example, if the alignment was TOP_RIGHT the top right of the element would be the same as the top right of this container)
    If not aligned to a corner (for example if the alignment was BOTTOM), then the centers would be aligned
    (the middle X of the element would be the same as the middle X of this container)
    """

    def __init__(self, size: Vec2 = None, relativePos: Vec2 = Vec2(0.0, 0.0), visible: bool = True, children: list[GUIElement] = None, childrenAlignments: list[str] = None):
        if size is None:
            size = window.getScreenSize()
        super().__init__(size, relativePos, visible, children)
        if childrenAlignments is None:
            childrenAlignments = []

        # ensures they are the same length
        for i in range(len(self.getChildren()) - len(childrenAlignments)):
            childrenAlignments.append("CENTER")
        childrenAlignments = childrenAlignments[:len(self.getChildren())]

        # sets all shorthand values to their full name or CENTER if not valid
        for i in range(len(childrenAlignments)):
            if childrenAlignments[i] in ALIGNMENT_SHORTHANDS:
                childrenAlignments[i] = VALID_ALIGNMENTS[i]
            elif childrenAlignments[i] not in VALID_ALIGNMENTS:
                childrenAlignments[i] = "CENTER"

        self.childrenAlignments = childrenAlignments

    def addChild(self, child: GUIElement, alignment: str = "CENTER"):
        super().addChild(child)

        if alignment in ALIGNMENT_SHORTHANDS:
            alignment = VALID_ALIGNMENTS[ALIGNMENT_SHORTHANDS.index(alignment)]

        self.childrenAlignments.append(alignment)

    def getAlignmentOfChild(self, child: GUIElement):
        assert child in self.getChildren(), "Element not a child of this container"
        return self.childrenAlignments[self.getChildren().index(child)]

    def getChildOffset(self, child: GUIElement):
        """return the offset of a specific child

        calculates the offset of a child based on its offset and returns it"""
        alignment = self.getAlignmentOfChild(child)

        if alignment == "TOP_LEFT":
            return super().getChildOffset(child) + Vec2(0, 0)
        elif alignment == "TOP":
            return super().getChildOffset(child) + Vec2((self.getSize().x - child.getSize().x) / 2, 0)
        elif alignment == "TOP_RIGHT":
            return super().getChildOffset(child) + Vec2(self.getSize().x - child.getSize().x, 0)
        elif alignment == "LEFT":
            return super().getChildOffset(child) + Vec2(0, self.getSize().y - child.getSize().y / 2)
        elif alignment == "CENTER":
            return super().getChildOffset(child) + Vec2((self.getSize().x - child.getSize().x) / 2, (self.getSize().y - child.getSize().y) / 2)
        elif alignment == "RIGHT":
            return super().getChildOffset(child) + Vec2(self.getSize().x - child.getSize().x, (self.getSize().y - child.getSize().y) / 2)
        elif alignment == "BOTTOM_LEFT":
            return super().getChildOffset(child) + Vec2(0, self.getSize().y - child.getSize().y)
        elif alignment == "BOTTOM":
            return super().getChildOffset(child) + Vec2((self.getSize().x - child.getSize().x) / 2, self.getSize().y - child.getSize().y)
        elif alignment == "BOTTOM_RIGHT":
            return super().getChildOffset(child) + Vec2(self.getSize().x - child.getSize().x, self.getSize().y - child.getSize().y)
        else:
            raise Exception("Not valid alignment: " + alignment)
