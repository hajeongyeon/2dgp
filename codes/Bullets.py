from pico2d import *

class Skill:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.6
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self):
        self.x, self.y = 500, 100
        self.frame = 0
        self.state = 1
        self.total_frames = 0.0
        if Skill.image == None:
            Skill.image = load_image('resource/character_skill_effect.png')

    def update(self, frame_time):
        self.total_frames += Skill.FRAMES_PER_ACTION * Skill.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 14

    def draw(self):
        self.image.clip_draw(self.frame * 339, self.state * 85, 339, 85, self.x, self.y)