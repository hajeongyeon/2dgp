from pico2d import *

class WaitingBackground:
    background = None
    portal = None

    def __init__(self):
        self.x = 450
        self.y = 130

        if WaitingBackground.background == None:
            WaitingBackground.background = load_image('resource/map_waiting.png')
        if WaitingBackground.portal == None:
            WaitingBackground.portal = load_image('resource/portal.png')
        self.bgm = load_music('sound/Waiting.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.background.draw(550, 300)
        self.portal.draw(815, 170)

    def ground_get_bb(self):
        return 400, 80, 1100, 80

    def portal_get_bb(self):
        return 815, 80, 845, 170

    def draw_bb(self):
        draw_rectangle(*self.ground_get_bb())
        draw_rectangle(*self.portal_get_bb())


class Stage1Background:
    TIME_PER_ACTION = 0.8
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    background = None
    portal = None
    foothold = None

    def __init__(self):
        self.cx = 50
        self.cy = 300
        if Stage1Background.background == None:
            Stage1Background.background = load_image('resource/map_stage1.png')
        if Stage1Background.portal == None:
            Stage1Background.portal = load_image('resource/portal.png')
        if Stage1Background.foothold == None:
            Stage1Background.foothold = load_image('resource/stage1foothold.png')
        self.bgm = load_music('sound/Stage1.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.speed = 0
        self.left = 0
        self.x = 0
        self.movex = 660
        self.total_frames = 0.0
        self.frame = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.background.w
        self.h = self.background.h
        self.height = 85
        self.dir = 1

    def set_center_object(self, character):
        self.set_center_object = character

    def draw(self):
        sx = self.x - self.left
        self.background.clip_draw_to_origin(self.left, 0, self.canvas_width, self.canvas_height, 0, 0)
        self.portal.clip_draw(0, 0, 87, 182, 1950 + sx, 195)
        #
        self.foothold.clip_draw(0, 0, 141, 86, 350 + sx, 200)
        self.foothold.clip_draw(0, 0, 141, 86, 470 + sx, 270)
        self.foothold.clip_draw(0, 0, 141, 86, 600 + sx, 340)
        self.foothold.clip_draw(0, 0, 141, 86, self.movex + sx, 270)
        self.foothold.clip_draw(0, 0, 141, 86, 970 + sx, 340)
        self.foothold.clip_draw(0, 0, 141, 86, 1090 + sx, 410)
        self.foothold.clip_draw(0, 0, 141, 86, 1220 + sx, 340)
        self.foothold.clip_draw(0, 0, 141, 86, 1340 + sx, 270)
        self.foothold.clip_draw(0, 0, 141, 86, 1460 + sx, 340)
        self.foothold.clip_draw(0, 0, 141, 86, 1580 + sx, 410)

    def update(self, frame_time):
        self.total_frames += Stage1Background.FRAMES_PER_ACTION * Stage1Background.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.left = clamp(0, int(self.set_center_object.x) - self.canvas_width//10, self.w - self.canvas_width)
        self.movex += (frame_time * self.dir * 80)
        if self.movex > 910:
            self.dir = -1
            self.movex = 910
        elif self.movex < 660:
            self.dir = 1
            self.movex = 660

    def ground1_get_bb(self):
        sx = self.x - self.left
        return 0 + sx, 170, 290 + sx, 170

    def ground2_get_bb(self):
        sx = self.x - self.left
        return 0 + sx, 70, 2016 + sx, 70

    def ground3_get_bb(self):
        sx = self.x - self.left
        return 1750 + sx, 110, 2016 + sx, 110

    def portal_get_bb(self):
        sx = self.x - self.left
        return 1950 + sx, 175, 1980 + sx, 175

    def foothold1_get_bb(self):
        sx = self.x - self.left
        return 290 + sx, 235, 410 + sx, 235

    def foothold2_get_bb(self):
        sx = self.x - self.left
        return 410 + sx, 305, 530 + sx, 305

    def foothold3_get_bb(self):
        sx = self.x - self.left
        return 530 + sx, 375, 650 + sx, 375

    def foothold4_get_bb(self):
        sx = self.x - self.left
        return self.movex - 60 + sx, 305, self.movex + 60 + sx, 305

    def foothold5_get_bb(self):
        sx = self.x - self.left
        return 910 + sx, 375, 1030 + sx, 375

    def foothold6_get_bb(self):
        sx = self.x - self.left
        return 1030 + sx, 445, 1150 + sx, 445

    def foothold7_get_bb(self):
        sx = self.x - self.left
        return 1160 + sx, 375, 1280 + sx, 375

    def foothold8_get_bb(self):
        sx = self.x - self.left
        return 1290 + sx, 305, 1410 + sx, 305

    def foothold9_get_bb(self):
        sx = self.x - self.left
        return 1410 + sx, 375, 1530 + sx, 375

    def foothold10_get_bb(self):
        sx = self.x - self.left
        return 1530 + sx, 445, 1650 + sx, 445

    def draw_bb(self):
        draw_rectangle(*self.portal_get_bb())
        draw_rectangle(*self.foothold1_get_bb())
        draw_rectangle(*self.foothold2_get_bb())
        draw_rectangle(*self.foothold3_get_bb())
        draw_rectangle(*self.foothold4_get_bb())
        draw_rectangle(*self.foothold5_get_bb())
        draw_rectangle(*self.foothold6_get_bb())
        draw_rectangle(*self.foothold7_get_bb())
        draw_rectangle(*self.foothold8_get_bb())
        draw_rectangle(*self.foothold9_get_bb())
        draw_rectangle(*self.foothold10_get_bb())
        draw_rectangle(*self.ground1_get_bb())
        draw_rectangle(*self.ground2_get_bb())
        draw_rectangle(*self.ground3_get_bb())

    def handle_event(self, event):
        pass


class Stage2Background:
    background = None
    foothold = None

    def __init__(self):
        self.x = 50
        self.y = 100
        if Stage2Background.background == None:
            Stage2Background.background = load_image('resource/map_stage2.png')
        if Stage2Background.foothold == None:
            Stage2Background.foothold = load_image('resource/stage2foothold.png')
        self.bgm = load_music('sound/Stage2.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def draw(self):
        self.background.draw(550, 300)
        self.foothold.clip_draw(0, 0, 129, 45, 90, 160)
        self.foothold.clip_draw(0, 0, 129, 45, 170, 230)
        self.foothold.clip_draw(0, 0, 129, 45, 1000, 330)

    def ground_get_bb(self):
        return 0, 100, 1100, 100

    def foothold1_get_bb(self):
        return 30, 178, 150, 178

    def foothold2_get_bb(self):
        return 106, 248, 226, 248

    def foothold3_get_bb(self):
        return 45, 315, 225, 315

    def foothold4_get_bb(self):
        return 133, 373, 253, 373

    def foothold5_get_bb(self):
        return 106, 435, 226, 435

    def foothold6_get_bb(self):
        return 845, 170, 966, 170

    def foothold7_get_bb(self):
        return 740, 228, 940, 228

    def foothold8_get_bb(self):
        return 858, 285, 978, 285

    def foothold9_get_bb(self):
        return 935, 348, 1054, 348

    def foothold10_get_bb(self):
        return 787, 412, 980, 412


    def draw_bb(self):
        draw_rectangle(*self.ground_get_bb())
        draw_rectangle(*self.foothold1_get_bb())
        draw_rectangle(*self.foothold2_get_bb())
        draw_rectangle(*self.foothold3_get_bb())
        draw_rectangle(*self.foothold4_get_bb())
        draw_rectangle(*self.foothold5_get_bb())
        draw_rectangle(*self.foothold6_get_bb())
        draw_rectangle(*self.foothold7_get_bb())
        draw_rectangle(*self.foothold8_get_bb())
        draw_rectangle(*self.foothold9_get_bb())
        draw_rectangle(*self.foothold10_get_bb())