import Game_Framework
import Main_State
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('resource/title.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_Framework.change_state(Main_State)



def draw():
    clear_canvas()
    image.draw(550, 300)
    update_canvas()




def update():
    pass


def pause():
    pass


def resume():
    pass






