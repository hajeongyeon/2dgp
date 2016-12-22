from pico2d import *

import Game_Framework
import Title_State

from Collision import *
from Background import Stage2Background
from Zakum import *
from Character import Character
from Bullets import Attack, Skill
from Time import *


name = "Stage2"
background = None
character = list()
running = True
font = None
time = None
zakumarm1 = list()
zakumarm2 = list()
zakumarm3 = list()
zakumarm4 = list()
zakumarm5 = list()
zakumarm6 = list()
zakumarm7 = list()
zakumarm8 = list()
zakumbody = list()


def enter():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8
    global font, skills, bullets, time

    time = Time()
    background = Stage2Background()
    zakumarm1.append(ZakumArm1())
    zakumarm2.append(ZakumArm2())
    zakumarm3.append(ZakumArm3())
    zakumarm4.append(ZakumArm4())
    zakumarm5.append(ZakumArm5())
    zakumarm6.append(ZakumArm6())
    zakumarm7.append(ZakumArm7())
    zakumarm8.append(ZakumArm8())
    zakumbody.append(ZakumBody())
    character.append(Character(background.x, background.y))
    skills = []
    bullets = []

    font = load_font('ENCR10B.TTF', 20)



def exit():
    global background, character, zakumbody, zakumarm1, zakumarm2, zakumarm3, zakumarm4, zakumarm5, zakumarm6, zakumarm7, zakumarm8
    global font, skills, bullets, time

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
    del(font)
    del(skills)
    del(bullets)
    del(time)


def shooting():
    global bullets
    for character_ in character:
        bullets.append(Attack(character_.x, character_.y, character_.state))


def skill():
    global skills
    for character_ in character:
        if character_.b_skill == True:
            skills.append(Skill(character_.x, character_.y, character_.state))



def gameclear():
    for character_ in character:
        character_.clear = True


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                for character_ in character:
                    if character_.death == True:
                        Game_Framework.change_state(Title_State)
                    if character_.clear == True:
                        Game_Framework.change_state(Title_State)
            else:
                for character_ in character:
                    character_.handle_event(event)
                    if character_.b_attack == True:
                        shooting()
                    elif character_.b_skill == True:
                        skill()


def update(frame_time):
    for character_ in character:
        character_.update(frame_time)
    time.update(frame_time)

    for zakumarm1_ in zakumarm1:
        zakumarm1_.update(frame_time)
    for zakumarm2_ in zakumarm2:
        zakumarm2_.update(frame_time)
    for zakumarm3_ in zakumarm3:
        zakumarm3_.update(frame_time)
    for zakumarm4_ in zakumarm4:
        zakumarm4_.update(frame_time)
    for zakumarm5_ in zakumarm5:
        zakumarm5_.update(frame_time)
    for zakumarm6_ in zakumarm6:
        zakumarm6_.update(frame_time)
    for zakumarm7_ in zakumarm7:
        zakumarm7_.update(frame_time)
    for zakumarm8_ in zakumarm8:
        zakumarm8_.update(frame_time)
    for zakumbody_ in zakumbody:
        zakumbody_.update(frame_time)

    for fire in skills:
        fire.update(frame_time)
    for attack in bullets:
        attack.update(frame_time)

    # character and foothold collide
    for character_ in character:
        if cag_collide(character_, background):
            character_.ground_collide2()
        if caf1_collide2(character_, background):
            character_.foothold1_collide2()
        if caf2_collide2(character_, background):
            character_.foothold2_collide2()
        if caf3_collide2(character_, background):
            character_.foothold3_collide2()
        if caf4_collide2(character_, background):
            character_.foothold4_collide2()
        if caf5_collide2(character_, background):
            character_.foothold5_collide2()
        if caf6_collide2(character_, background):
            character_.foothold6_collide2()
        if caf7_collide2(character_, background):
            character_.foothold7_collide2()
        if caf8_collide2(character_, background):
            character_.foothold8_collide2()
        if caf9_collide2(character_, background):
            character_.foothold9_collide2()
        if caf10_collide2(character_, background):
            character_.foothold10_collide2()

    # character and zakum collide
    for character_ in character:
        for zakumarm1_ in zakumarm1:
            if caza1_collide(character_, zakumarm1_):
                character_.hp -= 3
        for zakumarm2_ in zakumarm2:
            if caza2_collide(character_, zakumarm2_):
                character_.hp -= 3
        for zakumarm3_ in zakumarm3:
            if caza3_collide(character_, zakumarm3_):
                character_.hp -= 3
        for zakumarm4_ in zakumarm4:
            if caza4_collide(character_, zakumarm4_):
                character_.hp -= 3
        for zakumarm5_ in zakumarm5:
            if caza5_collide(character_, zakumarm5_):
                character_.hp -= 3
        for zakumarm6_ in zakumarm6:
            if caza6_collide(character_, zakumarm6_):
                character_.hp -= 3
        for zakumarm7_ in zakumarm7:
            if caza7_collide(character_, zakumarm7_):
                character_.hp -= 3
        for zakumarm8_ in zakumarm8:
            if caza8_collide(character_, zakumarm8_):
                character_.hp -= 3
        for zakumbody_ in zakumbody:
            if cazb_collide(character_, zakumbody_):
                character_.hp -= 3
            if zakumbody_.tf_skill1 == True:
                if zakumbody_.skilltime >= 0.65:
                    if skill1_collide1(character_, zakumbody_):
                        character_.hp -= 5
                    if skill1_collide2(character_, zakumbody_):
                        character_.hp -= 5
                    if skill1_collide3(character_, zakumbody_):
                        character_.hp -= 5
                    if skill1_collide4(character_, zakumbody_):
                        character_.hp -= 5
            if zakumbody_.tf_skill2 == True:
                if zakumbody_.skilltime >= 0.65:
                    if skill2_collide1(character_, zakumbody_):
                        character_.hp -= 7
                    if skill2_collide2(character_, zakumbody_):
                        character_.hp -= 7
                    if skill2_collide3(character_, zakumbody_):
                        character_.hp -= 7
                    if skill2_collide4(character_, zakumbody_):
                        character_.hp -= 7

    for character_ in character:
        if character_.hp <= 0:
            character_.death = True

        for zakumarm1_ in zakumarm1:
            if zakumarm1_.hp <= 0:
                zakumarm1.remove(zakumarm1_)
        for zakumarm2_ in zakumarm2:
            if zakumarm2_.hp <= 0:
                zakumarm2.remove(zakumarm2_)
        for zakumarm3_ in zakumarm3:
            if zakumarm3_.hp <= 0:
                zakumarm3.remove(zakumarm3_)
        for zakumarm4_ in zakumarm4:
            if zakumarm4_.hp <= 0:
                zakumarm4.remove(zakumarm4_)
        for zakumarm5_ in zakumarm5:
            if zakumarm5_.hp <= 0:
                zakumarm5.remove(zakumarm5_)
        for zakumarm6_ in zakumarm6:
            if zakumarm6_.hp <= 0:
                zakumarm6.remove(zakumarm6_)
        for zakumarm7_ in zakumarm7:
            if zakumarm7_.hp <= 0:
                zakumarm7.remove(zakumarm7_)
        for zakumarm8_ in zakumarm8:
            if zakumarm8_.hp <= 0:
                zakumarm8.remove(zakumarm8_)
        for zakumbody_ in zakumbody:
            if zakumbody_.hp <= 0:
                zakumbody.remove(zakumbody_)
                gameclear()
            else:
                if int(time.time % 10) == 0:
                    zakumbody_.skilling1()
                if int(time.time % 10) == 5:
                    zakumbody_.skilling2()

    # bullet and zakum collide
    for bullet in bullets:
        for zakumarm1_ in zakumarm1:
            if baza1_collide(bullet, zakumarm1_):
                zakumarm1_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm2_ in zakumarm2:
            if baza2_collide(bullet, zakumarm2_):
                zakumarm2_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm3_ in zakumarm3:
            if baza3_collide(bullet, zakumarm3_):
                zakumarm3_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm4_ in zakumarm4:
            if baza4_collide(bullet, zakumarm4_):
                zakumarm4_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm5_ in zakumarm5:
            if baza5_collide(bullet, zakumarm5_):
                zakumarm5_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm6_ in zakumarm6:
            if baza6_collide(bullet, zakumarm6_):
                zakumarm6_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm7_ in zakumarm7:
            if baza7_collide(bullet, zakumarm7_):
                zakumarm7_.hp -= 10000
                bullets.remove(bullet)
        for zakumarm8_ in zakumarm8:
            if baza8_collide(bullet, zakumarm8_):
                zakumarm8_.hp -= 10000
                bullets.remove(bullet)
        for zakumbody_ in zakumbody:
            if bazb_collide(bullet, zakumbody_):
                zakumbody_.hp -= 10000
                bullets.remove(bullet)

        # skill and zakum collide
    for fire in skills:
        for zakumarm1_ in zakumarm1:
            if saza1_collide(fire, zakumarm1_):
                zakumarm1_.hp -= 20000
                skills.remove(fire)
        for zakumarm2_ in zakumarm2:
            if saza2_collide(fire, zakumarm2_):
                zakumarm2_.hp -= 20000
                skills.remove(fire)
        for zakumarm3_ in zakumarm3:
            if saza3_collide(fire, zakumarm3_):
                zakumarm3_.hp -= 20000
                skills.remove(fire)
        for zakumarm4_ in zakumarm4:
            if saza4_collide(fire, zakumarm4_):
                zakumarm4_.hp -= 20000
                skills.remove(fire)
        for zakumarm5_ in zakumarm5:
            if saza5_collide(fire, zakumarm5_):
                zakumarm5_.hp -= 20000
                skills.remove(fire)
        for zakumarm6_ in zakumarm6:
            if saza6_collide(fire, zakumarm6_):
                zakumarm6_.hp -= 20000
                skills.remove(fire)
        for zakumarm7_ in zakumarm7:
            if saza7_collide(fire, zakumarm7_):
                zakumarm7_.hp -= 20000
                skills.remove(fire)
        for zakumarm8_ in zakumarm8:
            if saza8_collide(fire, zakumarm8_):
                zakumarm8_.hp -= 20000
                skills.remove(fire)
        for zakumbody_ in zakumbody:
            if sazb_collide(fire, zakumbody_):
                zakumbody_.hp -= 20000
                skills.remove(fire)


def draw(frame_time):
    clear_canvas()

    background.draw()
    for zakumarm1_ in zakumarm1:
        zakumarm1_.draw()
    for zakumarm2_ in zakumarm2:
        zakumarm2_.draw()
    for zakumarm3_ in zakumarm3:
        zakumarm3_.draw()
    for zakumarm4_ in zakumarm4:
        zakumarm4_.draw()
    for zakumarm5_ in zakumarm5:
        zakumarm5_.draw()
    for zakumarm6_ in zakumarm6:
        zakumarm6_.draw()
    for zakumarm7_ in zakumarm7:
        zakumarm7_.draw()
    for zakumarm8_ in zakumarm8:
        zakumarm8_.draw()
    for zakumbody_ in zakumbody:
        zakumbody_.draw()

    for character_ in character:
        character_.draw()

    #background.draw_bb()
    #for zakumarm1_ in zakumarm1:
        #zakumarm1_.draw_bb()
    #for zakumarm2_ in zakumarm2:
        #zakumarm2_.draw_bb()
    #for zakumarm3_ in zakumarm3:
        #zakumarm3_.draw_bb()
    #for zakumarm4_ in zakumarm4:
        #zakumarm4_.draw_bb()
    #for zakumarm5_ in zakumarm5:
        #zakumarm5_.draw_bb()
    #for zakumarm6_ in zakumarm6:
        #zakumarm6_.draw_bb()
    #for zakumarm7_ in zakumarm7:
        #zakumarm7_.draw_bb()
    #for zakumarm8_ in zakumarm8:
        #zakumarm8_.draw_bb()
    #for zakumbody_ in zakumbody:
        #zakumbody_.draw_bb()

    #for character_ in character:
        #character_.draw_bb()

    for attack in bullets:
        attack.draw()
        #attack.draw_bb()
    for skill in skills:
        skill.draw()
        #skill.draw_bb()

    #for character_ in character:
        #font.draw(character_.x - 30, character_.y + 40, 'hp : %d' % character_.hp)

    update_canvas()
