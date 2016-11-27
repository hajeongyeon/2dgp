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


class Portal:
    image = None

    def __init__(self):
        self.x, self.y = 815, 170
        if Portal.image == None:
            Portal.image = load_image('resource/portal.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x + 30, self.y - 90, self.x + 30, self.y

    def draw_bb(self):
        draw_rectangle(*self.get_bb())