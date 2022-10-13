from pico2d import *
import game_framework
import item_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = -1
        self.image = load_image('animation_sheet.png')
        self.item = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800 - self.item * 20:
            self.dir = -1
            self.x = 800 - self.item * 20
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        for i in range(0, self.item):
            if self.dir == 1:
                self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x + 20 * i, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x + 20 * i, self.y)
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)

#게임 초기화 : 객체들을 생성한다
boy = None # c로 따지면 NULL
grass = None

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

#게임 종료 - 객체 소멸
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()