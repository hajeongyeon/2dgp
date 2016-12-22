from pico2d import *

import Game_Framework
import Stage2_State

from Collision import *
from Background import *
from Character import Character

name = "Stage1"
background = None
character = list()


def create_world():
    global background, character

    background = Stage1Background()
    character.append(Character(background.cx, background.cy))

    for character_ in character:
        background.set_center_object(character_)


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
                for character_ in character:
                    if cap_collide(character_, background):
                        Game_Framework.change_state(Stage2_State)
            else:
                for character_ in character:
                    character_.handle_event(event)
                background.handle_event(event)


def update(frame_time):
    background.update(frame_time)

    for character_ in character:
        character_.update(frame_time)

    for character_ in character:
        if caf1_collide(character_, background):
            character_.foothold1_collide()
        if caf2_collide(character_, background):
            character_.foothold2_collide()
        if caf3_collide(character_, background):
            character_.foothold3_collide()
        if caf4_collide(character_, background):
            character_.foothold4_collide()
        if caf5_collide(character_, background):
            character_.foothold5_collide()
        if caf6_collide(character_, background):
            character_.foothold6_collide()
        if caf7_collide(character_, background):
            character_.foothold7_collide()
        if caf8_collide(character_, background):
            character_.foothold8_collide()
        if caf9_collide(character_, background):
            character_.foothold9_collide()
        if caf10_collide(character_, background):
            character_.foothold10_collide()
        if cag1_collide(character_, background):
            character_.ground1_collide()
        if cag2_collide(character_, background):
            character_.ground2_collide()
        if cag3_collide(character_, background):
            character_.ground3_collide()


def draw(frame_time):
    clear_canvas()

    background.draw()
    for character_ in character:
        character_.draw()

    background.draw_bb()
    for character_ in character:
        character_.draw_bb()

    update_canvas()