# The greedy strategy tries to play the best move it can only looking one step ahead
# It will not always find the shortest path...

def greedy(start, goal, visited, grid):
  # Get preferred x and y direction to the food
  vector = goal - start
  pref_x = clamp(vector.x, -1, 1)
  pref_y = clamp(vector.y, -1, 1)
  
  # Build a list of preferred next positions
  preferences = build_preferences(start, pref_x, pref_y)

  # Get the first valid preferred position
  for pos in preferences:
    if pos != start and pos not in visited:
      return [pos]

  # if no preference, do nothing
  return []

# Build a list of preferred next positions
def build_preferences(start, pref_x, pref_y):
  return [
    start.clone().move(pref_x, 0),
    start.clone().move(0, pref_y),
    start.clone().move(-pref_x, 0),
    start.clone().move(0, -pref_y)
  ]

def clamp(value, min_value, max_value):
  value = max(min_value, value)
  value = min(max_value, value)
  return value


