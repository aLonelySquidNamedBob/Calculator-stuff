from kandinsky import *

def apple(Xp, Yp):
  body = (0, 204, 0)
  bord = (0, 104, 0)
  red = (248, 0, 0) 
  red_dark = (200, 0, 0) 
  fill_rect(Xp,Yp+4,10,4,red_dark)
  fill_rect(Xp+2,Yp+2,6,8,red_dark)
  fill_rect(Xp+1,Yp+3,8,6,red)
  set_pixel(Xp+1,Yp+3,red_dark)
  set_pixel(Xp+1,Yp+8,red_dark)
  set_pixel(Xp+8,Yp+3,red)
  set_pixel(Xp+8,Yp+8,red_dark)
  fill_rect(Xp+2,Yp,3,1,bord)
  fill_rect(Xp+1,Yp+1,5,1,bord)
  fill_rect(Xp+2,Yp+1,2,1,body)
  fill_rect(Xp+3,Yp+2,3,1,body)

def tail(lsx, lsy, ld, c):
  x = lsx[0]
  y = lsy[0]
  d = ld[0]
  fill_rect(x,y,10,10,(0,0,0))
  if d == 0:
    fill_rect(x, y + 1, 3, 8, c)
    fill_rect(x + 3, y + 2, 3, 6, c)
    fill_rect(x + 6, y + 3, 2, 4, c)
    fill_rect(x + 8, y + 4, 2, 2, c)

  if d == 1:
    fill_rect(x, y + 4, 2, 2, c)
    fill_rect(x + 2, y + 3, 2, 4, c)
    fill_rect(x + 4, y + 2, 3, 6, c)
    fill_rect(x + 7, y + 1, 3, 8, c)
    
  if d == 3:
    fill_rect(x + 4, y, 2, 2, c)
    fill_rect(x + 3, y + 2, 4, 2, c)
    fill_rect(x + 2, y + 4, 6, 3, c)
    fill_rect(x + 1, y + 7, 8, 3, c)

  if d == 2:
    fill_rect(x + 1, y, 8, 3, c)
    fill_rect(x + 2, y + 3, 6, 3, c)
    fill_rect(x + 3, y + 6, 4, 2, c)
    fill_rect(x + 4, y + 8, 2, 2, c)

def head(x,y,d,c):
  if d == 0:
    fill_rect(x + 2, y + 2, 1, 6, c)
    fill_rect(x + 3, y + 1, 1, 8, c)
    fill_rect(x + 4, y, 6, 10, c)
    fill_rect(x + 4, y + 2, 2, 1, (0,0,0))
    fill_rect(x + 4, y + 7, 2, 1, (0,0,0))
    fill_rect(x, y + 4, 2, 2, (255,0,0))

  if d == 1:
    fill_rect(x, y, 6, 10, c)
    fill_rect(x + 6, y + 1, 1, 8, c)
    fill_rect(x + 7, y + 2, 1, 6, c)
    fill_rect(x + 4, y + 2, 2, 1, (0,0,0))
    fill_rect(x + 4, y + 7, 2, 1, (0,0,0))
    fill_rect(x + 8, y + 4, 2, 2, (255,0,0))
  
  if d == 3:
    fill_rect(x, y, 10, 6, c)
    fill_rect(x + 1, y + 6, 8, 1, c)
    fill_rect(x + 2, y + 7, 6, 1, c)
    fill_rect(x + 2, y + 4, 1, 2, (0,0,0))
    fill_rect(x + 7, y + 4, 1, 2, (0,0,0))
    fill_rect(x + 4,y + 8, 2, 2, (255,0,0))
  
  if d == 2:
    fill_rect(x + 2, y + 2, 6, 1, c)
    fill_rect(x + 1, y + 3, 8, 1, c)
    fill_rect(x, y + 4, 10, 6, c)
    fill_rect(x + 2, y + 4, 1, 2, (0,0,0))
    fill_rect(x + 7, y + 4, 1, 2, (0,0,0))
    fill_rect(x + 4, y, 2, 2, (255,0,0))

def grid(nx, ny, size, c):
  for x in range(10):
    for y in range(10):
      fill_rect(x * size, y * size, x + size - 1, y + size - 1, c)

grid(10,10,10,(0,0,0))
