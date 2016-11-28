from pico2d import *

class Character:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.6
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4


    image = None


    LEFT_STAND, RIGHT_STAND, LEFT_WALK, RIGHT_WALK, LEFT_ATTACK, RIGHT_ATTACK = 0, 1, 2, 3, 4, 5
    LEFT_JUMP, RIGHT_JUMP, LEFT_DEATH, RIGHT_DEATH = 6, 7, 8, 9


    def __init__(self):
        self.x, self.y = 100, 130
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0

        self.jumpy = 0
        self.temp = 0
        self.alert_frames = 0
        self.hp = 5000
        self.state = self.RIGHT_STAND
        if Character.image == None:
            Character.image = load_image('resource/character.png')


    def update(self, frame_time):
        self.life_time += frame_time
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

        if self.state == self.RIGHT_WALK:
            self.x = min(1100, self.x + distance)
        elif self.state == self.LEFT_WALK:
            self.x = max(0, self.x - distance)
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


    def draw(self):
        self.image.clip_draw(self.frame * 85, self.state * 85, 85, 85, self.x, self.y)


    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 20, self.y + 30


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


    def draw_bb(self):
        draw_rectangle(*self.get_bb())