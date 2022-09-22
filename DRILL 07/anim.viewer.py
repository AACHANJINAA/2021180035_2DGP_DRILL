from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
frame = 0  
    
while x < 800 : #오른쪽 달리기
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 6, 32, 32, x, 70)
     update_canvas()
     frame = (frame + 1) % 5
     x += 5
     delay(0.01)
     get_events()
     
while x > 0 : #왼쪽 달리기
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 7, 32, 32, x, 70)
     update_canvas()
     frame = (frame + 1) % 5
     x -= 5
     delay(0.01)
     get_events()

while x < 400 : #오른쪽 달리기
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 6, 32, 32, x, 70)
     update_canvas()
     frame = (frame + 1) % 5
     x += 5
     delay(0.01)
     get_events()

cnt = 0
while 1 : #앞으로 달리기
     if(cnt == 40):
        break
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 4, 32, 32, 400, 70)
     update_canvas()
     frame = (frame + 1) % 5
     delay(0.01)
     get_events()
     cnt += 1

cnt = 0
while 1 : #뒤로 달리기
     if(cnt == 40):
        break
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 5, 32, 32, 400, 70)
     update_canvas()
     frame = (frame + 1) % 5
     delay(0.01)
     get_events()
     cnt += 1
     
cnt = 0
while 1 : #앞으로 곡괭이 달리기
     if(cnt == 40):
        break
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 0, 32, 32, 400, 70)
     update_canvas()
     frame = (frame + 1) % 5
     delay(0.01)
     get_events()
     cnt += 1

cnt = 0
while 1 : #뒤로 곡괭이 달리기
     if(cnt == 40):
        break
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 1, 32, 32, 400, 70)
     update_canvas()
     frame = (frame + 1) % 5
     delay(0.01)
     get_events()
     cnt += 1

while x < 800 : #오른쪽 곡괭이 달리기
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 2, 32, 32, x, 70)
     update_canvas()
     frame = (frame + 1) % 5
     x += 5
     delay(0.01)
     get_events()

while x > 0 : #왼쪽 곡괭이 달리기
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 32, 32 * 3, 32, 32, x, 70)
     update_canvas()
     frame = (frame + 1) % 5
     x -= 5
     delay(0.01)
     get_events()


    



close_canvas()
