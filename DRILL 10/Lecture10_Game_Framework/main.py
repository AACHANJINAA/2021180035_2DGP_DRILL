from pico2d import *
import play_state
import logo_state
states = [logo_state, play_state] # 모듈을 변수로 취급

pico2d.open_canvas()

for state in states:
    state.enter()
    # game main loop code
    while state.running:
        state.handle_events()
        # 게임 월드의 객체를 업데이트 - 게임 로직
        state.update()
        # 게임 월드 렌더링
        state.draw()
        pico2d.delay(0.05)

exit()
# finalization code
pico2d.close_canvas()
