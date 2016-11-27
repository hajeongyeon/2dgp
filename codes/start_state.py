import Game_Framework
import Title_State
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1100, 600)
    image = load_image('resource/kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        Game_Framework.push_state(Title_State)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(550, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass




