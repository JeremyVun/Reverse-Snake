# Depth first search strategy
# Can sometimes be faster or slower than BFS

def dfs(start, goal, visited, grid):
  stack = [start]
  parents = {}
  #explored = []
  
  while stack:
    curr_pos = stack.pop(-1)
    #explored.append(curr_pos)
    
    # goal check
    if curr_pos == goal:
      path = get_path(start, goal, parents)
      return path
      #return path, explored
    
    # Explore children nodes
    elif curr_pos not in visited:
      visited.append(curr_pos)
      
      children = get_children(curr_pos, grid)
      
      for child in children:
        if child not in visited:
          stack.append(child)
          if (child not in parents):
            parents[child] = curr_pos
  
  path = get_path(start, goal, parents)
  return path
  #return path, explored


# Get neighbouring children of a current position
def get_children(currPos, grid):
  children = []

  # Get child to right of us
  if currPos.x < grid.num_cols - 1:
    child = currPos.clone().move(1, 0)
    children.append(child)
        
  # get child to left of us
  if currPos.x > 0:
    child = currPos.clone().move(-1, 0)
    children.append(child)
  
  # get child above us
  if currPos.y > 0:
    child = currPos.clone().move(0, -1)
    children.append(child)
  
  # get child below us
  if currPos.y < grid.num_rows - 1:
    child = currPos.clone().move(0, 1)
    children.append(child)
  
  return children

def get_path(start, end, parents):
  path = []
  
  current_square = end
  while (current_square != start):
    parent_square = parents[current_square]
    path.insert(0, current_square)
    current_square = parent_square
    
  return path