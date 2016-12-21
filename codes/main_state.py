from pico2d import *

import Game_Framework
import Stage1_State

from Collision import cap_collide, cag_collide
from Character import Character
from Background import WaitingBackground

name = "MainState"
background = None
character = None
attack = None
skill = None
bullets = None

def enter():
    global background, character
    background = WaitingBackground()
    character = Character()


def exit():
    global background, character
    del(background)
    del(character)


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


def update(frame_time):
    character.update(frame_time)

    if cag_collide(character, background):
        character.ground_collide()


def draw(frame_time):
    clear_canvas()

    background.draw()
    character.draw()

    background.draw_bb()
    character.draw_bb()

    update_canvas()