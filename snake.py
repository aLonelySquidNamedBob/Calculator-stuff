#modules
from kandinsky import *
from random import *
from time import *
from ion import *
from defs_for_snake import *

#colours
bla = (0, 0, 0)
whi = (255, 255, 255)
foo = (230, 0, 0)
sna = (30, 230, 30)

p = 0
point = -10
speed = 4
speed2 = 6


#setup
def grid():
  fill_rect(0, 0, 320, 222, whi)
  fill_rect(10, 20, 300, 190, bla)

def menu():
  global p
  global point
  global speed
  global speed2
  length2 = len("Score : " + str(point))*10/2
  fill_rect(0,0,320,222,whi)
  draw_string("Snake", 320//2-25, 40, (0,100,0))
  draw_string("Snake", 320//2-25+1, 40, (0,100,0))
  for x in range(2, 49):
    set_pixel(320//2-25+x, 57, (0,0,0))
  if p == 0:
    draw_string("Play", 320//2-20, 100)
    while True:
      draw_string("Speed : " + str(speed), 320//2-45, 130)
      if keydown(KEY_DOWN) and speed > 0:
        speed -= 1
        sleep(0.2)
      if keydown(KEY_UP) and speed < 9:
        speed += 1
        sleep(0.2)
      if keydown(KEY_OK) == True:
        speed2 = 11 - speed
        break
  else:
    draw_string("Game Over",320//2-45, 80, foo)
    draw_string("Play again : OK", 320//2-75, 140)
    draw_string("Score : " + str(point),320//2-int(length2),110)
    point = -10
    while True:
      draw_string("Speed : " + str(speed), 320//2-45, 170)
      if keydown(KEY_DOWN) and speed > 0:
        speed -= 1
        sleep(0.2)
      if keydown(KEY_UP) and speed < 9:
        speed += 1
        sleep(0.2)
      if keydown(KEY_OK) == True:
        speed2 = 11 - speed
        break

#features
def food():
  global fx
  global fy
  global lsx
  global lsy
  global f
  fx = randint(1, 30)*10
  fy = randint(2, 20)*10
  for ix, x in enumerate(lsx):
    if fx == x:
      for iy, y in enumerate(lsy):
        if fy == y and ix == iy:
            fx = randint(1, 30)*10
            fy = randint(2, 20)*10

  apple(fx, fy)
  f = 1

def points():
  global point
  draw_string("Points : "+str(point), 10, 0)

def direction():
  global direct
  global direct2
  if keydown(KEY_LEFT) and direct2 != 1:
    direct = 0
  elif keydown(KEY_RIGHT) and direct2 != 0:
    direct = 1
  elif keydown(KEY_UP) and direct2 != 3:
    direct = 2
  elif keydown(KEY_DOWN) and direct2 != 2:
    direct = 3

def snake():
  global sx
  global sy
  global lsx
  global lsy
  global direct
  global sna
  head(sx, sy, direct, sna)
  lsx.append(sx)
  lsy.append(sy)
  fill_rect(lsx[-2], lsy[-2], 10, 10, sna)

def move():
  global direct
  global sx
  global sy
  global fx
  global fy
  global f
  global length
  global mlength
  if direct == 0:
    sx -= 10
    snake()
    ld.append(direct)
  
  elif direct == 1:
    sx += 10
    snake()
    ld.append(direct)
  
  elif direct == 2:
    sy -= 10
    snake()
    ld.append(direct)
      
  elif direct == 3:
    sy += 10
    snake()
    ld.append(direct)
  
  if fx == sx:
    if fy == sy:
      mlength += 2
      f = 0
  
  length += 1

def delete():
  global mlength
  global length
  if length == mlength:
    fill_rect(lsx[0], lsy[0], 10, 10, bla)
    length -= 1
    lsx.pop(0)
    lsy.pop(0)
    
def gameover():
  global sx
  global sy
  global lsx
  global lsy
  if sx < 10 or sx > 300:
    return True
  elif sy < 20 or sy > 200:
    return True  
  
  lsxx = []
  lsyy = []
  for x in lsx:
    lsxx.append(x)
  for y in lsy:
    lsyy.append(y)
  lsxx.pop(-1)
  lsyy.pop(-1)
  for ix, x in enumerate(lsxx):
    if x == sx:
      for iy,y in enumerate(lsyy):
        if y == sy:
          if ix == iy:
            return True
          
  return False

#game
def update():
  global point
  global direct2
  global direct
  global lsx
  global lsy
  global ld
  while True:
    for i in range(speed2):
      direction()
      sleep(0.01)
    direct2 = direct
    move()
    delete()
    tail(lsx,lsy,ld,sna)
    if len(ld) > mlength - 2: 
      ld.pop(0)
    if f == 0:
      food()
      point += 10
    points()
    point += 1
    if gameover():
      break

#play again
try:
  while True:
    sx = 50
    sy = 50
    direct = 1
    direct2 = 1
    mlength = 4
    length = 0
    lsx = [320]
    lsy = [222]
    f = 0
    fx = 0
    fy = 0
    c = 0
    ld = []

    menu()
    grid()
    update()
    p += 1
    
except KeyboardInterrupt:
  fill_rect(0,0,320,222,whi)
