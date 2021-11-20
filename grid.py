from pygame import draw
from pygame import Rect
from pos import Pos

# The game grid
# Implement me first so we have something to render
class Grid:
  def __init__(self, screen, num_rows, num_cols, box_size, line_width=1):
    # The pygame screen object used for rendering
    self.screen = screen

    self.num_rows = num_rows
    self.num_cols = num_cols
    self.box_size = box_size
    self.line_width = line_width

  # Render the grid
  def render(self):
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        self.render_pos(Pos(i, j), 'white', self.line_width)

  # Render a grid position
  def render_pos(self, pos, color, line_width=0):
    box = self.create_box(pos)
    draw.rect(self.screen, color, box, line_width)

  # Create a Pygame rectangle for rendering
  def create_box(self, pos):
    box_pos = (self.box_size * pos.x, self.box_size * pos.y)
    box_dims = (self.box_size, self.box_size)
    return Rect(box_pos, box_dims)

  # clamp an x, y position within the grid
  # Used by objects to stay on the grid
  # EXTENSION: allow screen wrap around instead
  def clamp(self, pos):
    pos.x = max(0, pos.x)
    pos.x = min(pos.x, self.num_cols - 1)

    pos.y = max(0, pos.y)
    pos.y = min(pos.y, self.num_rows - 1)

    return pos
