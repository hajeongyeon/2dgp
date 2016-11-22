from pico2d import *

import Game_Framework
import Stage1_State

from Character import Character
from Background import WaitingBackground

name = "MainState"
background = None
character = None


def enter():
    global background, character
    background = WaitingBackground()
    character = Character()


def exit():
    global background, character
    del(background)
    del(character)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                Game_Framework.change_state(Stage1_State)
            else:
                character.handle_event(event)


def update():
    character.update()
    delay(0.1)


def draw():
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass