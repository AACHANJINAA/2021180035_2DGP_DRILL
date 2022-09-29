from pico2d import *


def handle_events():
    global running
    global dir_lr, dir_ud, framey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                framey = 1
                dir_lr += 1
            elif event.key == SDLK_LEFT:
                framey = 0
                dir_lr -= 1
            elif event.key == SDLK_UP:
                if framey == 3:
                    framey = 1
                dir_ud += 1
            elif event.key == SDLK_DOWN:
                if framey == 2:
                    framey = 0
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                framey = 3
                dir_lr -= 1
            elif event.key == SDLK_LEFT:
                framey = 2
                dir_lr += 1
            elif event.key == SDLK_UP:
                framey = 3
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                framey = 2
                dir_ud += 1


open_canvas(800, 600)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 600 // 2
framex = 0
framey = 3
dir_lr = 0
dir_ud = 0

while running:
    clear_canvas()
    grass.draw(1280 // 2, 1024 // 2)
    character.clip_draw(framex * 100, framey * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    framex = (framex + 1) % 8
    if x <= 30:
        x = 40
    elif x >= 770:
        x = 760
    else:
        x += dir_lr * 5

    if y <= 30:
        y = 40
    elif y >= 570:
        y = 560
    else:
        y += dir_ud * 5
    delay(0.01)

close_canvas()