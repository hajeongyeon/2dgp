from pico2d import *

import Game_Framework
import Stage1_State

from Collision import collide
from Character import Character
from Background import WaitingBackground, Portal

name = "MainState"
background = None
character = None
portal = None


def enter():
    global background, character, portal
    background = WaitingBackground()
    portal = Portal()
    character = Character()


def exit():
    global background, character, portal
    del(background)
    del(portal)
    del(character)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            else:
                character.handle_event(event)


def update(frame_time):
    character.update(frame_time)

    if collide(character, portal):
        Game_Framework.change_state(Stage1_State)


def draw(frame_time):
    clear_canvas()

    background.draw()
    portal.draw()
    character.draw()

    portal.draw_bb()
    character.draw_bb()

    update_canvas()