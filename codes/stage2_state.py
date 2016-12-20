from pico2d import *

import Game_Framework
import Main_State

from Collision import caf1_collide2, caf2_collide2, caf3_collide2, caf4_collide2, caf5_collide2, caf6_collide2, caf7_collide2, caf8_collide2, caf9_collide2, caf10_collide2, caza1_collide, caza2_collide, caza3_collide, caza4_collide, caza5_collide, caza6_collide, caza7_collide, caza8_collide
from Background import Stage2Background
from Zakum import ZakumBody, ZakumArm1, ZakumArm2, ZakumArm3, ZakumArm4, ZakumArm5, ZakumArm6, ZakumArm7, ZakumArm8, ZakumSkillEffect1, ZakumSkillEffect2
from Character import Character

name = "Stage2"
background = None
character = None
running = True
font = None


def enter():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8
    global zskill1, zskill2, font

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

    font = load_font('ENCR10B.TTF', 20)



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

    if caf1_collide2(character, background):
        character.foothold1_collide2()
    if caf2_collide2(character, background):
        character.foothold2_collide2()
    if caf3_collide2(character, background):
        character.foothold3_collide2()
    if caf4_collide2(character, background):
        character.foothold4_collide2()
    if caf5_collide2(character, background):
        character.foothold5_collide2()
    if caf6_collide2(character, background):
        character.foothold6_collide2()
    if caf7_collide2(character, background):
        character.foothold7_collide2()
    if caf8_collide2(character, background):
        character.foothold8_collide2()
    if caf9_collide2(character, background):
        character.foothold9_collide2()
    if caf10_collide2(character, background):
        character.foothold10_collide2()

    if caza1_collide(character, zakumarm1):
        character.hp -= 30
    if caza2_collide(character, zakumarm2):
        character.hp -= 30
    if caza3_collide(character, zakumarm3):
        character.hp -= 30
    if caza4_collide(character, zakumarm4):
        character.hp -= 30
    if caza5_collide(character, zakumarm5):
        character.hp -= 30
    if caza6_collide(character, zakumarm6):
        character.hp -= 30
    if caza7_collide(character, zakumarm7):
        character.hp -= 30
    if caza8_collide(character, zakumarm8):
        character.hp -= 30


def draw(frame_time):
    clear_canvas()

    for i in zskill1:
        i.draw()
    for j in zskill2:
        j.draw()

    zakumarm1.draw_bb()
    zakumarm2.draw_bb()
    zakumarm3.draw_bb()
    zakumarm4.draw_bb()
    zakumarm5.draw_bb()
    zakumarm6.draw_bb()
    zakumarm7.draw_bb()
    zakumarm8.draw_bb()

    background.draw()
    character.draw()

    zakumarm1.draw()
    zakumarm2.draw()
    zakumarm3.draw()
    zakumarm4.draw()
    zakumarm5.draw()
    zakumarm6.draw()
    zakumarm7.draw()
    zakumarm8.draw()
    zakumbody.draw()

    background.draw_bb()
    character.draw_bb()

    zakumbody.draw_bb()


    font.draw(character.x - 30, character.y + 40, 'hp : %4d' % character.hp)

    update_canvas()
