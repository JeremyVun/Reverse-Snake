from pygame import *

# You play as the food
# Implement me second after the grid
class Food:
  def __init__(self, pos, grid):
    self.pos = pos
    self.grid = grid
    self.color = Color(0, 255, 0)

    #self.pos_changed = False
    self.is_dead = False

  
  # Apply player controls
  def update(self):
    for e in event.get():
      if e.type == KEYDOWN:
        if (e.key == K_RIGHT):
          self.pos.move(1, 0)
        if (e.key == K_LEFT):
          self.pos.move(-1, 0)
        if (e.key == K_UP):
          self.pos.move(0, -1)
        if (e.key == K_DOWN):
          self.pos.move(0, 1)

    self.pos = self.grid.clamp(self.pos)

  # Render the player
  def render(self):
    self.pos = self.grid.clamp(self.pos)
    self.grid.render_pos(self.pos, 'green')
