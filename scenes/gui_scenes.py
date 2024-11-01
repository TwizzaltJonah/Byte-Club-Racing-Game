from scenes.scenes import Scene, switchCurrentSceneByType
from guis.interactable_guis import ImageButton
from general_utils.vec2 import Vec2
from guis.base_guis import RootContainer
from guis.image_guis import GUIImage
from guis.container_guis import AlignmentContainer
from pygame_rendering import window

class MainMenuScene(Scene):

    def __init__(self):
        super().__init__(RootContainer(children=[
            AlignmentContainer(children=[
                ImageButton("sprites/play_button.png", size=Vec2(512, 256), onUp=switchCurrentSceneByType, onUpArgs=(TestScene,)),
            ], childrenAlignments=[
                "CENTER"
            ])
        ]))

class TestScene(Scene):

    def __init__(self):
        self.testImage1 = GUIImage("sprites/SpriteTest.png", size=Vec2(640, 640))
        self.testImage2 = GUIImage("sprites/SpriteTest.png", size=Vec2(320, 320))

        super().__init__(RootContainer(children=[
            AlignmentContainer(children=[
                self.testImage1,
                self.testImage2
            ], childrenAlignments=[
                "TL",
                "R"
            ])
        ]))

    def onFrame(self):
        super().onFrame()
        self.testImage1.rotateBy(window.getDelta() * 57)
        self.testImage2.rotateBy(window.getDelta() * -32)
