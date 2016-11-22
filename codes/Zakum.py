from pico2d import *

import random


class ZakumBody:
    image = None


    def __init__(self):
        self.x, self.y = 485, 345
        self.frame = 0
        self.hp = 900000
        if ZakumBody.image == None:
            ZakumBody.image = load_image('resource/zakum_body.png')


    def update(self):
        self.frame = (self.frame + 1) % 8


    def draw(self):
        self.image.clip_draw(self.frame * 419, 0, 415, 400, self.x, self.y)


class ZakumArm1:
    image = None


    def __init__(self):
        self.x, self.y = 620, 460
        self.frame = 0
        self.hp = 200000
        if ZakumArm1.image == None:
            ZakumArm1.image = load_image('resource/zakum_arm1.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 301, 0, 301, 237, self.x, self.y)


class ZakumArm2:
    image = None


    def __init__(self):
        self.x, self.y = 650, 420
        self.frame = 0
        self.hp = 200000
        if ZakumArm2.image == None:
            ZakumArm2.image = load_image('resource/zakum_arm2.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 310, 0, 310, 237, self.x, self.y)


class ZakumArm3:
    image = None


    def __init__(self):
        self.x, self.y = 650, 370
        self.frame = 0
        self.hp = 200000
        if ZakumArm3.image == None:
            ZakumArm3.image = load_image('resource/zakum_arm3.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 315, 0, 325, 237, self.x, self.y)


class ZakumArm4:
    image = None


    def __init__(self):
        self.x, self.y = 650, 300
        self.frame = 0
        self.hp = 200000
        if ZakumArm4.image == None:
            ZakumArm4.image = load_image('resource/zakum_arm4.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 325, 0, 328, 237, self.x, self.y)


class ZakumArm5:
    image = None


    def __init__(self):
        self.x, self.y = 370, 460
        self.frame = 0
        self.hp = 200000
        if ZakumArm5.image == None:
            ZakumArm5.image = load_image('resource/zakum_arm5.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 300, 237, self.x, self.y)


class ZakumArm6:
    image = None


    def __init__(self):
        self.x, self.y = 350, 420
        self.frame = 0
        self.hp = 200000
        if ZakumArm6.image == None:
            ZakumArm6.image = load_image('resource/zakum_arm6.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 320, 0, 320, 237, self.x, self.y)


class ZakumArm7:
    image = None


    def __init__(self):
        self.x, self.y = 350, 370
        self.frame = 0
        self.hp = 200000
        if ZakumArm7.image == None:
            ZakumArm7.image = load_image('resource/zakum_arm7.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 333, 0, 328, 237, self.x, self.y)


class ZakumArm8:
    image = None


    def __init__(self):
        self.x, self.y = 350, 300
        self.frame = 0
        self.hp = 200000
        if ZakumArm8.image == None:
            ZakumArm8.image = load_image('resource/zakum_arm8.png')


    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 330, 0, 330, 237, self.x, self.y)


class ZakumSkillEffect1:
    image = None


    def __init__(self):
        self.x, self.y = random.randint(0, 1100), 300
        self.frame = 0
        self.time = 0
        if ZakumSkillEffect1.image == None:
            ZakumSkillEffect1.image = load_image('resource/zakum_skill_effect1.png')


    def update(self):
        self.frame = (self.frame + 1) % 9
        self.time += 1


    def draw(self):
        if(self.time > 72):
            self.image.clip_draw(self.frame * 320, 0, 320, 600, self.x, self.y)
        if(self.time == 79):
            self.time = 0
            self.x = random.randint(0, 1100)


class ZakumSkillEffect2:
    image = None


    def __init__(self):
        self.x, self.y = random.randint(0, 1100), 300
        self.frame = 0
        self.time = 0
        if ZakumSkillEffect2.image == None:
            ZakumSkillEffect2.image = load_image('resource/zakum_skill_effect2.png')


    def update(self):
        self.frame = (self.frame + 1) % 7
        self.time += 1


    def draw(self):
        if(self.time > 100):
            self.image.clip_draw(self.frame * 80, 0, 80, 600, self.x, self.y)
        if self.time == 106:
            self.time = 0
            self.x = random.randint(0, 1100)