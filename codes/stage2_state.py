from pico2d import *

import game_framework
import main_state

name = "Stage2State"

background = None
character = None

class Background:
    image = None

    def __init__(self):
        if Background.image == None:
            Background.image = load_image('resource/map_stage2.png')

    def draw(self):
        self.image.draw(550, 300)

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


class Character:
    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_WALK, LEFT_WALK, RIGHT_ATTACK, LEFT_ATTACK = 0, 1, 2, 3, 4, 5
    RIGHT_JUMP, LEFT_JUMP, RIGHT_ALERT, LEFT_ALERT, RIGHT_SKILL, LEFT_SKILL = 6, 7, 8, 9, 10, 11

    def __init__(self):
        self.x, self.y = 100, 188
        self.frame = 0
        self.jumpy = 0
        self.temp = 0
        self.alert_frames = 0
        self.hp = 5000
        self.state = self.RIGHT_STAND
        if Character.image == None:
            Character.image = load_image('resource/character.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.state == self.RIGHT_WALK:
            self.x = min(1100, self.x + 10)
        elif self.state == self.LEFT_WALK:
            self.x = max(0, self.x - 10)
        elif self.state == self.LEFT_JUMP:
            if (self.jumpy <= 20):
                self.jumpy += 20
                self.y += self.jumpy
            else:
                self.y = self.temp
                self.jumpy = 0
                self.state = self.LEFT_STAND
        elif self.state == self.RIGHT_JUMP:
            if (self.jumpy <= 20):
                self.jumpy += 20
                self.y += self.jumpy
            else:
                self.y = self.temp
                self.jumpy = 0
                self.state = self.RIGHT_STAND
        elif self.state == self.LEFT_ALERT:
            self.alert_frames += 1
            if (self.alert_frames == 20):
                self.state = self.LEFT_STAND
                self.alert_frames = 0
        elif self.state == self.RIGHT_ALERT:
            self.alert_frames += 1
            if (self.alert_frames == 20):
                self.state = self.RIGHT_STAND
                self.alert_frames = 0


    def draw(self):
        self.image.clip_draw(self.frame * 173, self.state * 100, 167, 100, self.x, self.y)


    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_WALK
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_WALK
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_WALK,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_WALK,):
                self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            if self.state in (self.RIGHT_WALK, self.RIGHT_STAND):
                self.state = self.RIGHT_ATTACK
            if self.state in (self.LEFT_WALK, self.LEFT_STAND):
                self.state = self.LEFT_ATTACK
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_STAND
            if self.state in (self.LEFT_ATTACK,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LALT):
            if self.state in (self.RIGHT_STAND,):
                self.temp = self.y
                self.state = self.RIGHT_JUMP
            if self.state in (self.LEFT_STAND,):
                self.temp = self.y
                self.state = self.LEFT_JUMP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state in (self.RIGHT_STAND, self.RIGHT_ATTACK, self.RIGHT_WALK):
                self.state = self.RIGHT_ALERT
            if self.state in (self.LEFT_STAND, self.LEFT_ATTACK, self.LEFT_WALK):
                self.state = self.LEFT_ALERT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LSHIFT):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_SKILL
            if self.state in (self.LEFT_ATTACK,):
                self.state = self.LEFT_SKILL


class character_skill_effect_2:
    image = None

    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = 0
        if character_skill_effect_2.image == None:
            character_skill_effect_2.image = load_image('resource/character_skill_effect2.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        if self.frame == 5:
            character_skill_effect_2.remove(character_skill_effect_2)

    def draw(self):
        self.image.clip_draw(self.frame * 255, 0, 255, 113, self.x, self.y)


character = None
running = True


def enter():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8, skill2

    background = Background()
    zakumarm1 = ZakumArm1()
    zakumarm2 = ZakumArm2()
    zakumarm3 = ZakumArm3()
    zakumarm4 = ZakumArm4()
    zakumarm5 = ZakumArm5()
    zakumarm6 = ZakumArm6()
    zakumarm7 = ZakumArm7()
    zakumarm8 = ZakumArm8()
    zakumbody = ZakumBody()
    character = Character()
    skill2 = character_skill_effect_2()


def exit():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8, skill2

    del(background)
    del(zakumarm1)
    del(zakumarm2)
    del(zakumarm3)
    del(zakumarm4)
    del(zakumarm5)
    del(zakumarm6)
    del(zakumarm7)
    del(zakumarm8)
    del(zakumbody)
    del(character)
    del(skill2)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(main_state)
            else:
                character.handle_event(event)


def update():
    zakumarm1.update()
    zakumarm2.update()
    zakumarm3.update()
    zakumarm4.update()
    zakumarm5.update()
    zakumarm6.update()
    zakumarm7.update()
    zakumarm8.update()
    zakumbody.update()
    character.update()
    skill2.update()
    delay(0.1)


def draw():
    clear_canvas()

    background.draw()
    zakumarm1.draw()
    zakumarm2.draw()
    zakumarm3.draw()
    zakumarm4.draw()
    zakumarm5.draw()
    zakumarm6.draw()
    zakumarm7.draw()
    zakumarm8.draw()
    zakumbody.draw()
    character.draw()
    skill2.draw()

    update_canvas()
