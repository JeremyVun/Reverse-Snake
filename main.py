import pygame
from pygame.time import Clock
from game import GameFactory
from config.config import config

width = config["width"]
height = config["height"]
box_size = config["box_size"]

def main():
  pygame.init()

  # Use clock to set an fps
  clock = Clock()

  # Create the game screen
  screen = pygame.display.set_mode((width, height))
  
  # Create and run the snake game
  fac = GameFactory()
  game = fac.create(screen, width, height, box_size)

  while not game.is_game_over():
    screen.fill((0, 0, 0))
    
    game.update()
    game.render()
    
    pygame.display.flip()
    clock.tick(10)

  print(f"Game is over! Score={game.score}")

main()