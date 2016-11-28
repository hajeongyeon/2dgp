from pico2d import *

import Game_Framework
import Main_State

from Background import Stage2Background
from Zakum import ZakumBody, ZakumArm1, ZakumArm2, ZakumArm3, ZakumArm4, ZakumArm5, ZakumArm6, ZakumArm7, ZakumArm8, ZakumSkillEffect1, ZakumSkillEffect2
from Character import Character

name = "Stage2"
background = None
character = None
running = True


def enter():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8
    global zskill1, zskill2

    background = Stage2Background()
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
    zskill1 = [ZakumSkillEffect1() for i in range(5)]
    zskill2 = [ZakumSkillEffect2() for j in range(5)]


def exit():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8
    global zskill1, zskill2

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
    del(zskill1)
    del(zskill2)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                Game_Framework.change_state(Main_State)
            else:
                character.handle_event(event)


def update(frame_time):
    zakumarm1.update(frame_time)
    zakumarm2.update(frame_time)
    zakumarm3.update(frame_time)
    zakumarm4.update(frame_time)
    zakumarm5.update(frame_time)
    zakumarm6.update(frame_time)
    zakumarm7.update(frame_time)
    zakumarm8.update(frame_time)
    zakumbody.update(frame_time)
    character.update(frame_time)
    for i in zskill1:
        i.update(frame_time)
    for j in zskill2:
        j.update(frame_time)


def draw(frame_time):
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
    for i in zskill1:
        i.draw()
    for j in zskill2:
        j.draw()

    update_canvas()
