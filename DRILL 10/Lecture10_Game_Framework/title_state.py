from pico2d import *

import game_framework
import play_state

image = None
title_time = 0.0

def enter():
    global image, title_time
    image = load_image('title.png')
    title_time = 0.0
    pass

def exit():
    global image
    del image
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    global title_time
    delay(0.05)
    title_time += 0.05
    if title_time > 1.0:
        game_framework.change_state(play_state)
    pass

def pause():
    game_framework.quit()
    pass

def resume():
    pass






