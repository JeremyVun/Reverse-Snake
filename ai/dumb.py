# A dumb AI that makes the snake go in random direction
# Returns explored, path

import random
from .dfs import get_children

def dumb(start, goal, visited, grid):
  children = get_children(start, grid)
  random.shuffle(children)

  # return first valid child
  for child in children:
    if child != start and child not in visited:
      return [child]
  
  # return no path
  return []
