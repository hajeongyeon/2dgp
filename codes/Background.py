from pico2d import *

class WaitingBackground:
    image = None

    def __init__(self):
        if WaitingBackground.image == None:
            WaitingBackground.image = load_image('resource/map_waiting.png')

    def draw(self):
        self.image.draw(550, 300)


class Stage1Background:
    image = None

    def __init__(self):
        if Stage1Background.image == None:
            Stage1Background.image = load_image('resource/map_stage1.png')

    def draw(self):
        self.image.draw(1200, 300)


class Stage2Background:
    image = None

    def __init__(self):
        if Stage2Background.image == None:
            Stage2Background.image = load_image('resource/map_stage2.png')

    def draw(self):
        self.image.draw(550, 300)