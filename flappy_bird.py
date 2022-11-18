from kandinsky import *
from ion import *
import random
import time


class bird:
  def __init__(self):
    self.size = 8
    self.coords = [50, 100]
    self.l_coords = [50, 100]
    
    self.green = (96, 248, 96)
    
    self.g = 9
    
    self.alive = True
        
    self.v_y = 0
  
  def draw(self):
    fill_rect(self.l_coords[0], int(self.l_coords[1]), self.size, int(self.l_coords[1]) - int(self.coords[1]) - 1, (255,255,255))
    fill_rect(self.l_coords[0], int(self.l_coords[1] + self.size), self.size, int(self.l_coords[1]) - int(self.coords[1]) + 1, (255,255,255))
    fill_rect(self.coords[0], int(self.coords[1]), self.size, self.size, (240,230,0))
  
  def getInput(self, vy):
    if keydown(KEY_OK):
      return -1.15
    else:
      return vy
  
  def gameover(self):
    if self.coords[1] > 222 - self.size or self.coords[1] < 0:
      self.alive = False
    elif get_pixel(int(self.coords[0] + self.size), int(self.coords[1])) == self.green:
      self.alive = False
    elif get_pixel(int(self.coords[0] + self.size), int(self.coords[1] + self.size)) == self.green:
      self.alive = False
    elif get_pixel(int(self.coords[0]), int(self.coords[1])) == self.green:
      self.alive = False
    elif get_pixel(int(self.coords[0]), int(self.coords[1]) + self.size) == self.green:
      self.alive = False
  
  def update(self, dt, d=False, c=0):
    self.l_coords[1] = self.coords[1]
    self.coords[1] += self.v_y
    self.v_y += self.g * dt
    if d:
      time.sleep(0.01)
      if c == 0:
        self.v_y = -2
      pass
    else:
      self.v_y = self.getInput(self.v_y)

class new_pipe:
  def __init__(self, height, green):
    self.width = 30
    self.height = height
    self.distanceY = 55
    self.speed = 1
    
    self.green = green
    
    self.x = 320
    self.y = self.height
    
  def draw(self):
    last_x = self.x + self.width + self.speed
    fill_rect(self.x, self.y, self.width, -self.height, self.green)
    fill_rect(self.x, self.y + self.distanceY, self.width, 222 - (self.y + self.distanceY), self.green)
    fill_rect(last_x, self.y, self.speed, -self.height, (255,255,255))
    fill_rect(last_x, self.y + self.distanceY, self.speed, 222 - (self.y + self.distanceY), (255,255,255))
  
  def update(self, dt):
    self.x -= self.speed

def play():
  green = (100, 250, 100)
  
  b = bird()
  pipes = []
  
  score = 0
  counter = 0
  distance_between_pipes = 115
  
  dt = 0.1

  while b.alive:
    t = time.monotonic()
    if counter % distance_between_pipes == 0:
      p = new_pipe(random.randint(20, 150), green)
      pipes.append(p)
      score += 1
    for pipe in pipes:
      pipe.update(dt)
      pipe.draw()
      if pipe.x < -pipe.width:
        del pipe
        pipes.pop(0)
    
    draw_string(str(score), 150, 10)
    
    b.update(dt)
    b.gameover()
    b.draw()
    
    counter += 1
    
    dt = time.monotonic() - t
  
  counter = 0
  
  while b.coords[1] < 222:
    t = time.monotonic()
    b.update(dt, True, counter)
    b.draw()
    counter += 1
    dt = time.monotonic() - t
  
  time.sleep(0.3)

def menu():
  playing = False
  
  fill_rect(0, 0, 320, 222, (255, 255, 255))
  draw_string("Flappy Bird", 105, 40, (50, 150, 50))
  draw_string("PLAY", 140, 150)
  draw_bird(142, 100)
  while not playing:
    if keydown(KEY_OK):
      playing = True
      fill_rect(0, 0, 320, 222, (255, 255, 255))
      play()
  
def draw_bird(x, y):
  size = 2
  
  bird = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0, 0], 
          [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
          [0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0], 
          [1, 3, 3, 3, 3, 1, 2, 2, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0], 
          [1, 3, 3, 3, 3, 3, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0], 
          [1, 2, 3, 3, 3, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 5, 5, 5, 5, 5, 5, 1], 
          [0, 0, 1, 1, 1, 4, 4, 4, 4, 1, 5, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 1, 0], 
          [0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
  
  for i in range(len(bird)):
    for j in range(len(bird[0])):
      if bird[i][j] == 1:
        fill_rect(x + j * size, y + i * size, size, size, (0, 0, 0))
      if bird[i][j] == 2:
        fill_rect(x + j * size, y + i * size, size, size, (255, 245, 0))
      if bird[i][j] == 3:
        fill_rect(x + j * size, y + i * size, size, size, (255, 250, 200))
      if bird[i][j] == 4:
        fill_rect(x + j * size, y + i * size, size, size, (255, 200, 0))
      if bird[i][j] == 5:
        fill_rect(x + j * size, y + i * size, size, size, (200, 60, 60))

while True:
  menu()
