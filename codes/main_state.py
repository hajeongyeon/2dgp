from pico2d import *

import Game_Framework
import Stage1_State

from Collision import *
from Character import Character
from Background import WaitingBackground

name = "MainState"
background = None
character = list()
attack = None
skill = None
bullets = None

def enter():
    global background, character
    background = WaitingBackground()
    character.append(Character(background.x, background.y))


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
                for character_ in character:
                    if cap_collide(character_, background):
                        Game_Framework.change_state(Stage1_State)
            else:
                for character_ in character:
                    character_.handle_event(event)


def update(frame_time):
    for character_ in character:
        character_.update(frame_time)

    for character_ in character:
        if cag_collide(character_, background):
            character_.ground_collide()


def draw(frame_time):
    clear_canvas()

    background.draw()
    for character_ in character:
        character_.draw()

    #background.draw_bb()
    #for character_ in character:
        #character_.draw_bb()

    update_canvas()