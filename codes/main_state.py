from pico2d import *

import Game_Framework
import Stage1_State

from Collision import collide
from Character import Character
from Background import WaitingBackground
from Bullets import Skill

name = "MainState"
background = None
character = None
skill = None

def enter():
    global background, character, skill
    background = WaitingBackground()
    character = Character()
    skill = Skill()


def exit():
    global background, character, skill
    del(background)
    del(character)
    del(skill)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if collide(character, background):
                    Game_Framework.change_state(Stage1_State)
            else:
                character.handle_event(event)


def update(frame_time):
    character.update(frame_time)
    skill.update(frame_time)


def draw(frame_time):
    clear_canvas()

    background.draw()
    character.draw()
    skill.draw()

    background.draw_bb()
    character.draw_bb()

    update_canvas()