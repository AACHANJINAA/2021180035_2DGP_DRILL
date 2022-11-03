from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

q = 400
w = 90

def move_rect(x, y):
    while (x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.007)
        
    while (y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.007)
          
    while (x > 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.007)

    while (y >= 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.007)   

def move_circle(x, y):
     a = 0
     b = 0
     cnt = 0
     while (1):
         if cnt <= 90:
             a += 3
             b += 2.25
         elif cnt > 90 & cnt <= 180 :
             a -= 3
             b += 2.25
         elif cnt > 180 & cnt <= 270:
             a -= 3
             b -= 2.25
         elif cnt > 270 & cnt < 360:
             a += 3
             b -= 2.25
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x + a, y + b)
         delay(0.01)
         cnt += 1
         if cnt == 360:
            cnt = 0
            a = 0
            b = 0
     
            
while(1):
    move_rect(q, w)
    move_circle(q, w)

close_canvas()
