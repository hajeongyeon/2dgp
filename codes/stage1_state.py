from pico2d import *

import Game_Framework
import Stage2_State

from Collision import collide
from Background import *
from Character import Character

name = "Stage1"
background = None
character = None


def create_world():
    global background, character

    character = Character()
    background = Stage1Background()

    background.set_center_object(character)

def destroy_world():
    global background, character

    del(character)
    del(background)


def enter():
    Game_Framework.reset_time()
    create_world()


def exit():
    destroy_world()


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
                    Game_Framework.change_state(Stage2_State)
            else:
                character.handle_event(event)
                background.handle_event(event)


def update(frame_time):
    character.update(frame_time)
    background.update(frame_time)


def draw(frame_time):
    clear_canvas()

    background.draw()
    character.draw()

    background.draw_bb()
    character.draw_bb()

    update_canvas()