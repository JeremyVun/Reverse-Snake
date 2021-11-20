from pos import Pos
from grid import Grid
from food import Food
from snake import Snake

# Different Snake Brains
from brain import *

# Wrapper class for the Snake Game
class SnakeGame:
  def __init__(self, grid, snake, food):
    self.grid = grid
    self.snake = snake
    self.food = food
    self.score = 0

  # Update the state of the game
  # using common interfaces for update() and render(), we don't have to implement everything at first
  def update(self):
    self.snake.update()
    self.food.update()
    self.score += 1
  
  # Render the current state of the game
  def render(self):
    self.snake.render()
    self.food.render()
    self.grid.render()

  # Check if the game is over
  def is_game_over(self):
    return self.snake.is_dead or self.food.is_dead

# Factory for creating the game
class GameFactory():
  def create(self, screen, width, height, box_size, line_width=1):
    num_rows = int(height/box_size)
    num_cols = int(width/box_size)

    # Create the game grid
    grid = Grid(screen, num_rows, num_cols, box_size)

    # Create the food
    food_pos = Pos(3,3)
    food = Food(food_pos, grid)

    # Create the snake
    snake_pos = Pos(8, 8)
    snake_length = 5
    snake_brain = bfs_brain()
    snake_speed = 0.2

    snake = Snake(snake_pos, snake_length, snake_speed, snake_brain, food, grid)

    # Create the Snake game!
    return SnakeGame(grid, snake, food)
