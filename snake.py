from pos import Pos
from config.config import config

drawPath = config["draw_path"]
drawExplored = config["draw_explored"]

# The Snake class
# Implement the snake third, after food
class Snake:
  def __init__(self, pos, length, speed, brain, food, grid):
    self.food = food
    self.grid = grid

    self.body = self.build_body(pos, length)
    self.brain = brain

    self.speed = speed
    self.movement_charge = 0
    self.growth_charge = 0
    self.is_dead = False

    """ self.explored = [] """
    self.path = []

  # Initialise our snake body
  def build_body(self, head, length):
    result = [head]

    for i in range(1, length):
      body_part = Pos(head.x - i, head.y)
      body_part = self.grid.clamp(body_part)
      result.append(body_part)

    return result

  # Update the state of the snake every so often
  def update(self):
    self.movement_charge += self.speed
    self.growth_charge += self.speed

    # Kill the food if we ate it
    for pos in self.body:
      if pos == self.food.pos:
        self.food.is_dead = True

    # Move
    if self.movement_charge > 1:
      self.movement_charge = 0
      self.speed *= 1.02

      # Activate the brain to get a path
      self.path = self.think()
      #self.path, self.explored = self.think()

      # Move along path generated by the brain
      if (len(self.path) > 0):
        self.body.insert(0, self.path.pop(0))
      else:
        self.is_dead = True
      
      # Grow the body
      if (self.growth_charge < 3):
        self.body.pop(-1)
      else:
        self.growth_charge = 0

  # Render the snake
  def render(self):
    # Render squared explored by the brain
    #if drawExplored:
      #for pos in self.explored:
        #self.grid.render_pos(pos, 'grey')

    # Render the snake's planned path
    if drawPath:
      for pos in self.path:
        self.grid.render_pos(pos, 'blue')

    # Render the snake
    for pos in self.body[1:]:
      self.grid.render_pos(pos, 'orange')

    # Render the snake head
    self.grid.render_pos(self.body[0], 'red')

  # Activate the snake brain to get a path
  def think(self):
    # return self.head.clone().move(0, -1)
    return self.brain.find_path(self.body, self.food, self.grid)
    