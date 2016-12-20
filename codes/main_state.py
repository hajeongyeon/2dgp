from pico2d import *

import Game_Framework
import Stage1_State

from Collision import cap_collide, cag_collide
from Character import Character
from Background import WaitingBackground
from Bullets import Attack, Skill

name = "MainState"
background = None
character = None
attack = None
skill = None
bullets = None

def enter():
    global background, character, skills, attack, bullets
    background = WaitingBackground()
    character = Character()
    skills = []
    bullets = []


def exit():
    global background, character, skills, attack, bullets
    del(background)
    del(character)
    del(skills)
    del(attack)
    del(bullets)


def shooting():
    global bullets
    bullets.append(Attack(character.x, character.y, character.state))


def skill():
    global skills
    skills.append(Skill(character.x, character.y, character.state))


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if cap_collide(character, background):
                    Game_Framework.change_state(Stage1_State)
            else:
                character.handle_event(event)
                if character.b_attack == True:
                    shooting()
                elif character.b_skill == True:
                    skill()


def update(frame_time):
    character.update(frame_time)

    for skill in skills:
        skill.update(frame_time)
    for attack in bullets:
        attack.update(frame_time)

    if cag_collide(character, background):
        character.ground_collide()


def draw(frame_time):
    clear_canvas()

    background.draw()
    character.draw()

    for attack in bullets:
        attack.draw()
        attack.draw_bb()
    for skill in skills:
        skill.draw()
        skill.draw_bb()

    background.draw_bb()
    character.draw_bb()

    update_canvas()