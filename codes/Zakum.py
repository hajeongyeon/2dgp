from pico2d import *

import random


class ZakumBody:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 485, 325
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 900000
        if ZakumBody.image == None:
            ZakumBody.image = load_image('resource/zakum_body.png')

    def get_bb(self):
        return 400, 160, 600, 525


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumBody.FRAMES_PER_ACTION * ZakumBody.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 419, 0, 415, 400, self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class ZakumArm1:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 620, 460
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm1.image == None:
            ZakumArm1.image = load_image('resource/zakum_arm1.png')


    def get_bb(self):
        return 485, 345, 770, 575


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm1.FRAMES_PER_ACTION * ZakumArm1.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 301, 0, 301, 237, self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class ZakumArm2:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 650, 420
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm2.image == None:
            ZakumArm2.image = load_image('resource/zakum_arm2.png')

    def get_bb(self):
        return 515, 305, 800, 535

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm2.FRAMES_PER_ACTION * ZakumArm2.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 310, 0, 310, 237, self.x, self.y)


class ZakumArm3:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 650, 370
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm3.image == None:
            ZakumArm3.image = load_image('resource/zakum_arm3.png')

    def get_bb(self):
        return 515, 255, 800, 485

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm3.FRAMES_PER_ACTION * ZakumArm3.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 315, 0, 325, 237, self.x, self.y)


class ZakumArm4:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 650, 300
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm4.image == None:
            ZakumArm4.image = load_image('resource/zakum_arm4.png')


    def get_bb(self):
        return 515, 185, 800, 415


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm4.FRAMES_PER_ACTION * ZakumArm4.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 325, 0, 328, 237, self.x, self.y)


class ZakumArm5:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 370, 460
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm5.image == None:
            ZakumArm5.image = load_image('resource/zakum_arm5.png')


    def get_bb(self):
        return 235, 345, 520, 575


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm5.FRAMES_PER_ACTION * ZakumArm5.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 300, 237, self.x, self.y)


class ZakumArm6:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 350, 420
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm6.image == None:
            ZakumArm6.image = load_image('resource/zakum_arm6.png')


    def get_bb(self):
        return 215, 305, 500, 535


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm6.FRAMES_PER_ACTION * ZakumArm6.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 320, 0, 320, 237, self.x, self.y)


class ZakumArm7:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 350, 370
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm7.image == None:
            ZakumArm7.image = load_image('resource/zakum_arm7.png')


    def get_bb(self):
        return 215, 255, 500, 485


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm7.FRAMES_PER_ACTION * ZakumArm7.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 333, 0, 328, 237, self.x, self.y)


class ZakumArm8:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    def __init__(self):
        self.x, self.y = 350, 300
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 200000
        if ZakumArm8.image == None:
            ZakumArm8.image = load_image('resource/zakum_arm8.png')


    def get_bb(self):
        return 215, 185, 500, 415


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm8.FRAMES_PER_ACTION * ZakumArm8.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 330, 0, 330, 237, self.x, self.y)


class ZakumSkillEffect1:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 9


    image = None


    def __init__(self):
        self.x, self.y = random.randint(0, 1100), 330
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        if ZakumSkillEffect1.image == None:
            ZakumSkillEffect1.image = load_image('resource/zakum_skill_effect1.png')


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumSkillEffect1.FRAMES_PER_ACTION * ZakumSkillEffect1.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 9


    def draw(self):
        self.image.clip_draw(self.frame * 252, 0, 252, 474, self.x, self.y)
        if self.frame == 8:
            self.x = random.randint(0, 1100)


class ZakumSkillEffect2:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7


    image = None


    def __init__(self):
        self.x, self.y = random.randint(0, 1100), 330
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        if ZakumSkillEffect2.image == None:
            ZakumSkillEffect2.image = load_image('resource/zakum_skill_effect2.png')


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumSkillEffect2.FRAMES_PER_ACTION * ZakumSkillEffect2.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7


    def draw(self):
        self.image.clip_draw(self.frame * 63, 0, 63, 474, self.x, self.y)
        if self.frame == 6:
            self.x = random.randint(0, 1100)