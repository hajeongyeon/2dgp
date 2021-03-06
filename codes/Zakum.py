from pico2d import *

import random


class ZakumBody:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    ZB_SPEED_KMPH = 20.0  # Km / Hour
    ZB_SPEED_MPM = (ZB_SPEED_KMPH * 1000.0 / 60.0)
    ZB_SPEED_MPS = (ZB_SPEED_MPM / 60.0)
    ZB_SPEED_PPS = (ZB_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    FRAMES_PER_SKILL = 12
    SKILL_PER_TIME = 1.0 / 1.5


    image = None
    skill1 = None
    skill2 = None


    def __init__(self):
        self.x, self.y = 485, 325
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.hp = 900000
        #
        self.death = False
        #
        self.skilltime = 0
        self.skill1_frame = 0
        self.skill2_frame = 0
        self.tf_skill1 = False
        self.tf_skill2 = False
        self.total_skill1 = 0.0
        self.total_skill2 = 0.0

        if ZakumBody.image == None:
            ZakumBody.image = load_image('resource/zakum_body.png')
        if ZakumBody.skill1 == None:
            ZakumBody.skill1 = load_image('resource/zakum_skill_effect1.png')
        if ZakumBody.skill2 == None:
            ZakumBody.skill2 = load_image('resource/zakum_skill_effect2.png')

    def get_bb(self):
        return 400, 160, 600, 525

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumBody.FRAMES_PER_ACTION * ZakumBody.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.skill1_frame = int(self.total_skill1) % 9
        self.skill2_frame = int(self.total_skill2) % 7

        if self.tf_skill1 == True:
            self.total_skill1 += ZakumBody.FRAMES_PER_SKILL * ZakumBody.SKILL_PER_TIME * frame_time
            self.skilltime += frame_time
            if self.skilltime >= 1.0:
                self.total_skill1 = 0
                self.skilltime = 0
                self.tf_skill1 = False

        if self.tf_skill2 == True:
            self.total_skill2 += ZakumBody.FRAMES_PER_SKILL * ZakumBody.SKILL_PER_TIME * frame_time
            self.skilltime += frame_time
            if self.skilltime >= 1.0:
                self.total_skill2 = 0
                self.skilltime = 0
                self.tf_skill2 = False

    def skilling1(self):
        self.tf_skill1 = True

    def skilling2(self):
        self.tf_skill2 = True

    def draw(self):
        self.image.clip_draw(self.frame * 419, 0, 415, 400, self.x, self.y)
        if self.tf_skill1 == True:
            self.skill1.clip_draw(self.skill1_frame * 253, 0, 253, 474, 100, 300)
            self.skill1.clip_draw(self.skill1_frame * 253, 0, 253, 474, 350, 300)
            self.skill1.clip_draw(self.skill1_frame * 253, 0, 253, 474, 600, 300)
            self.skill1.clip_draw(self.skill1_frame * 253, 0, 253, 474, 850, 300)
        if self.tf_skill2 == True:
            self.skill2.clip_draw(self.skill2_frame * 64, 0, 64, 474, 200, 300)
            self.skill2.clip_draw(self.skill2_frame * 64, 0, 64, 474, 450, 300)
            self.skill2.clip_draw(self.skill2_frame * 64, 0, 64, 474, 700, 300)
            self.skill2.clip_draw(self.skill2_frame * 64, 0, 64, 474, 950, 300)

    def get_skill_1(self):
        if self.skilltime >= 0.65:
            return 50, 100, 150, 200
    def get_skill_2(self):
        if self.skilltime >= 0.65:
            return 250, 100, 350, 200
    def get_skill_3(self):
        if self.skilltime >= 0.65:
            return 450, 100, 550, 200
    def get_skill_4(self):
        if self.skilltime >= 0.65:
            return 650, 100, 750, 200
    def get_skill_5(self):
        if self.skilltime >= 0.65:
            return 150, 100, 250, 580
    def get_skill_6(self):
        if self.skilltime >= 0.65:
            return 350, 100, 450, 580
    def get_skill_7(self):
        if self.skilltime >= 0.65:
            return 550, 100, 650, 580
    def get_skill_8(self):
        if self.skilltime >= 0.65:
            return 750, 100, 850, 580

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        if self.tf_skill1 == True:
            if self.skilltime >= 0.65:
                draw_rectangle(*self.get_skill_1())
                draw_rectangle(*self.get_skill_2())
                draw_rectangle(*self.get_skill_3())
                draw_rectangle(*self.get_skill_4())
        if self.tf_skill2 == True:
            if self.skilltime >= 0.65:
                draw_rectangle(*self.get_skill_5())
                draw_rectangle(*self.get_skill_6())
                draw_rectangle(*self.get_skill_7())
                draw_rectangle(*self.get_skill_8())


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
        self.death = False
        if ZakumArm1.image == None:
            ZakumArm1.image = load_image('resource/zakum_arm1.png')


    def get_bb(self):
        return 785, 345, 785, 575


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
        self.death = False
        if ZakumArm2.image == None:
            ZakumArm2.image = load_image('resource/zakum_arm2.png')

    def get_bb(self):
        return 815, 305, 815, 535

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
        self.death = False
        if ZakumArm3.image == None:
            ZakumArm3.image = load_image('resource/zakum_arm3.png')

    def get_bb(self):
        return 820, 255, 820, 485

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
        self.death = False
        if ZakumArm4.image == None:
            ZakumArm4.image = load_image('resource/zakum_arm4.png')


    def get_bb(self):
        return 825, 185, 825, 415


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
        self.death = False
        if ZakumArm5.image == None:
            ZakumArm5.image = load_image('resource/zakum_arm5.png')


    def get_bb(self):
        return 235, 345, 235, 575


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
        self.death = False
        if ZakumArm6.image == None:
            ZakumArm6.image = load_image('resource/zakum_arm6.png')


    def get_bb(self):
        return 225, 305, 225, 535


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
        self.death = False
        if ZakumArm7.image == None:
            ZakumArm7.image = load_image('resource/zakum_arm7.png')


    def get_bb(self):
        return 220, 255, 220, 485


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
        self.death = False
        if ZakumArm8.image == None:
            ZakumArm8.image = load_image('resource/zakum_arm8.png')


    def get_bb(self):
        return 215, 185, 215, 415


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += ZakumArm8.FRAMES_PER_ACTION * ZakumArm8.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 330, 0, 330, 237, self.x, self.y)