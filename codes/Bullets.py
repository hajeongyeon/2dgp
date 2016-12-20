from pico2d import *

class Attack:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    ATTACK_SPEED_KMPH = 60.0  # Km / Hour
    ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
    ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
    ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    ATTACK_SPEED = 5

    LEFT_ATTACK, RIGHT_ATTACK = 4, 5

    image = None

    def __init__(self, x, y, state):
        self.x, self.y = x, y + 30
        self.dir = 1
        self.state = state
        self.attack = False
        if self.state in (self.RIGHT_ATTACK,):
            self.dir = 1
        elif self.state in (self.LEFT_ATTACK,):
            self.dir = -1
        if Attack.image == None:
            Attack.image = load_image('resource/bullet.png')


    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def update(self, frame_time):
        speed = Attack.ATTACK_SPEED_PPS * frame_time
        self.x += (self.dir * speed)

    def draw(self):
        self.image.clip_draw(0, 0, 13, 13, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class Skill:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    ATTACK_SPEED_KMPH = 60.0  # Km / Hour
    ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
    ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
    ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    ATTACK_SPEED = 5

    LEFT_ATTACK, RIGHT_ATTACK = 4, 5
    image = None

    def __init__(self, x, y, state):
        self.x, self.y = x, y
        self.attack = False
        self.frame = 0
        self.sstate = state
        self.cstate = 0
        self.dir = 1
        self.total_frames = 0.0
        if self.sstate == self.RIGHT_ATTACK:
            self.cstate = 0
            self.dir = 1
        elif self.sstate == self.LEFT_ATTACK:
            self.cstate = 1
            self.dir = -1
        if Skill.image == None:
            Skill.image = load_image('resource/character_skill_effect.png')

    def update(self, frame_time):
        self.total_frames += Skill.FRAMES_PER_ACTION * Skill.ACTION_PER_TIME * frame_time
        speed = Attack.ATTACK_SPEED_PPS * frame_time
        self.x += (self.dir * speed)
        self.frame = int(self.total_frames) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 70, self.cstate * 50, 70, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
