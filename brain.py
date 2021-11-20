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
    visited = body[1:]
    goal = food.pos

    # Use the injected strategy
    path = self.strategy(start, goal, visited, grid)
    #path, explored = self.strategy(start, goal, visited, grid)

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