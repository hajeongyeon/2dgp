import game_framework
import stage2_state
from pico2d import *

name = "Stage1State"
character = None

class Character:
    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_WALK, LEFT_WALK, RIGHT_ATTACK, LEFT_ATTACK = 0, 1, 2, 3, 4, 5
    RIGHT_JUMP, LEFT_JUMP, RIGHT_ALERT, LEFT_ALERT, RIGHT_SKILL, LEFT_SKILL = 6, 7, 8, 9, 10, 11

    def __init__(self):
        self.x, self.y = 100, 100
        self.frame = 0
        self.jumpy = 0
        self.temp = 0
        self.alert_frames = 0
        self.state = self.RIGHT_STAND
        if Character.image == None:
            Character.image = load_image('character.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.state == self.RIGHT_WALK:
            self.x = min(800, self.x + 10)
        elif self.state == self.LEFT_WALK:
            self.x = max(0, self.x - 10)
        elif self.state == self.LEFT_JUMP:
            if (self.jumpy <= 20):
                self.jumpy += 20
                self.y += self.jumpy
            else:
                self.y = self.temp
                self.jumpy = 0
                self.state = self.LEFT_STAND
        elif self.state == self.RIGHT_JUMP:
            if (self.jumpy <= 20):
                self.jumpy += 20
                self.y += self.jumpy
            else:
                self.y = self.temp
                self.jumpy = 0
                self.state = self.RIGHT_STAND
        elif self.state == self.LEFT_ALERT:
            self.alert_frames += 1
            if (self.alert_frames == 20):
                self.state = self.LEFT_STAND
                self.alert_frames = 0
        elif self.state == self.RIGHT_ALERT:
            self.alert_frames += 1
            if (self.alert_frames == 20):
                self.state = self.RIGHT_STAND
                self.alert_frames = 0



    def draw(self):
        self.image.clip_draw(self.frame * 173, self.state * 100, 167, 100, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_WALK
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_WALK
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_WALK,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_WALK,):
                self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            if self.state in (self.RIGHT_WALK, self.RIGHT_STAND):
                self.state = self.RIGHT_ATTACK
            if self.state in (self.LEFT_WALK, self.LEFT_STAND):
                self.state = self.LEFT_ATTACK
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_STAND
            if self.state in (self.LEFT_ATTACK,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LALT):
            if self.state in (self.RIGHT_STAND,):
                self.temp = self.y
                self.state = self.RIGHT_JUMP
            if self.state in (self.LEFT_STAND,):
                self.temp = self.y
                self.state = self.LEFT_JUMP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state in (self.RIGHT_STAND, self.RIGHT_ATTACK, self.RIGHT_WALK):
                self.state = self.RIGHT_ALERT
            if self.state in (self.LEFT_STAND, self.LEFT_ATTACK, self.LEFT_WALK):
                self.state = self.LEFT_ALERT


def enter():
    global character
    open_canvas(1000, 600)
    character = Character()


def exit():
    global character
    del(character)
    close_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(stage2_state)
            else:
                character.handle_event(event)


def update():
    character.update()
    delay(0.1)


def draw():
    clear_canvas()
    character.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass