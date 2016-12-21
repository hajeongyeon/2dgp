import Game_Framework
import Title_State

from pico2d import *


name = "HowtoplayState"
image = None


def enter():
    global image
    image = load_image('resource/howtoplay.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_Framework.change_state(Title_State)



def draw(frame_time):
    clear_canvas()
    image.draw(550, 300)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass