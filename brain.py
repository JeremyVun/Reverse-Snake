from ai.dumb import dumb
from ai.bfs import bfs
from ai.dfs import dfs
from ai.greedy import greedy

# The Snakes brain tries to find a path to the player using an injected strategy
class Brain:
  def __init__(self, strategy):
    self.strategy = strategy

  def find_path(self, body, food, grid):
    start = body[0]
    visited = {bodypart:True for bodypart in body[1:]}
    goal = food.pos

    # Use the injected strategy
    parents = self.strategy(start, goal, visited, grid)
    path = self.get_path(start, goal, parents)
    path.remove(start)

    return path


  def get_path(self, start, end, parents):
    path = []

    current_square = end
    while (current_square != start):
      parent_square = parents[current_square]
      path.insert(0, parent_square)
      current_square = parent_square
      
    return path


# Factory functions for creating different types of Snake Brains
def dumb_brain():
  print("Snake is using Dumb Pathfinding")
  return Brain(dumb)

def greedy_brain():
  print("Snake is using Greedy Pathfinding!")
  return Brain(greedy)

def bfs_brain():
  print("Snake is using BFS Pathfinding!")
  return Brain(bfs)

def dfs_brain():
  print("Snake is using DFS Pathfinding!")
  return Brain(dfs)