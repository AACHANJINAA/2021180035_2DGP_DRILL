from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, AD, AU, TIMER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYUP, SDLK_a): AU,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
}

class SLEEP:
    @staticmethod
    def enter(self, event):
        print("ENTER SLEEP:")
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print("EXIT SLEEP")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:  # 오른쪽을 바라보고 있는 상태
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '',
                                           self.x, self.y - 20, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, 'v',
                                           self.x, self.y - 20, 100, 100)
        pass
class IDLE:
    @staticmethod
    def enter(self, event):
        print("ENTER IDLE:")
        self.dir = 0
        # 타이머 설정
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print("EXIT IDLE")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: #시간이 경과하면,
            #이벤트를 발생시켜주어야 한다. TIMER
            #self.q.insert(0, TIMER) #객체지향프로그래밍에 위배, q를 직접 엑세스하고있으니까
            self.add_event(TIMER) # 객체지향적인 방법
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: #오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass
class RUN:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    def exit(self):
        self.face_dir = self.dir

        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass
class AUTO_RUN:
    def enter(self, event):
        self.cnt = 0
        if event == AD:
            self.UP_a = False
            self.DOWN_a = True
        elif event == AU:
            self.UP_a = True
            self.DOWN_a = False
        pass

    def exit(self):
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        if self.x >= 700:
            self.dir = -1
        elif self.x <= 100:
            self.dir = +1
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        if self.UP_a:
            self.add_event(AU)
        elif self.DOWN_a:
            self.add_event(AD)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass

next_state = {
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP, AD: IDLE, AU: AUTO_RUN},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: IDLE, AU: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, AD: IDLE, AU: AUTO_RUN},
    AUTO_RUN: {RD: RUN, LD: RUN, RU: IDLE, LU: IDLE, AD: IDLE, AU: AUTO_RUN},
}


class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):  # 소년이 스스로 이벤트를 처리할 수 있게,,,
        # event는 키이벤트... 이것을 내부 RD 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)  # 변환된 내부 이벤트를 q에 추가

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # q에 먼가 들어있다면
            event = self.q.pop()  # 이벤트를 가져오고
            self.cur_state.exit(self)  # 현재상태를 나가고
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 나간다.
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

# 클래스를 이용해서 상태를 만듦
