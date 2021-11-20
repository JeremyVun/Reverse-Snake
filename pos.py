# A Position utility class to help us write cleaner code
class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Create a clone of ourselves
  def clone(self):
    return Pos(self.x, self.y)
  
  # Move the position by specified x, y
  def move(self, x, y):
    self.x += x
    self.y += y
    return self

  # Subtract two positions from each other
  def __sub__(self, other):
    return Pos(self.x - other.x, self.y - other.y)

  # Compare with another Pos object
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __hash__(self):
    return (self.x, self.y).__hash__()

  # Print us a pretty string
  def __str__(self):
    return f"<x: {self.x}, y: {self.y}>"

  # Print us a pretty string
  def __repr__(self):
    return f"({self.x}, {self.y})"