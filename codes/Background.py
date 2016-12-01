from pico2d import *

class WaitingBackground:
    background = None
    portal = None

    def __init__(self):
        if WaitingBackground.background == None:
            WaitingBackground.background = load_image('resource/map_waiting.png')
        if WaitingBackground.portal == None:
            WaitingBackground.portal = load_image('resource/portal.png')

    def draw(self):
        self.background.draw(550, 300)
        self.portal.draw(815, 170)

    def get_bb(self):
        return 815, 80, 845, 170

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Stage1Background:
    TIME_PER_ACTION = 0.8
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    background = None
    portal = None

    def __init__(self):
        if Stage1Background.background == None:
            Stage1Background.background = load_image('resource/map_stage1.png')
        if Stage1Background.portal == None:
            Stage1Background.portal = load_image('resource/portal.png')

        self.speed = 0
        self.left = 0
        self.x = 0
        self.total_frames = 0.0
        self.frame = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.background.w
        self.h = self.background.h
        self.height = 85

    def set_center_object(self, character):
        self.set_center_object = character

    def draw(self):
        sx = self.x - self.left
        self.background.clip_draw_to_origin(self.left, 0, self.canvas_width, self.canvas_height, 0, 0)
        self.portal.clip_draw(0, 0, 87, 182, 1950 + sx, 195)

    def update(self, frame_time):
        self.total_frames += Stage1Background.FRAMES_PER_ACTION * Stage1Background.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.left = clamp(0, int(self.set_center_object.x) - self.canvas_width//10, self.w - self.canvas_width)

    def get_bb(self):
        sx = self.x - self.left
        return 1950 + sx, 105, 1980 + sx, 195

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass


class Stage2Background:
    image = None

    def __init__(self):
        if Stage2Background.image == None:
            Stage2Background.image = load_image('resource/map_stage2.png')

    def draw(self):
        self.image.draw(550, 300)