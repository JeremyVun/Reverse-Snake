# Breadth first search strategy
# It will always find shortest path

def bfs(start, goal, visited, grid):
  queue = [start]
  parents = {}
  #explored = []
  
  while queue:
    curr_pos = queue.pop(0)
    #explored.append(curr_pos)
    
    if (curr_pos == goal):
      path = get_path(start, goal, parents)
      return path
      #return path, explored
    
    if (curr_pos not in visited):
      # get the node to the right of us
      if (curr_pos.x < grid.num_cols - 1):
        child = curr_pos.clone().move(1, 0)
        queue.append(child)
        if (child not in parents):
          parents[child] = curr_pos
      
      # get the node to the left of us
      if (curr_pos.x > 0):
        child = curr_pos.clone().move(-1, 0)
        queue.append(child)
        if (child not in parents):
          parents[child] = curr_pos
      
      # get the node above us
      if (curr_pos.y > 0):
        child = curr_pos.clone().move(0, -1)
        queue.append(child)
        if (child not in parents):
          parents[child] = curr_pos
       
      # get the node below us
      if (curr_pos.y < grid.num_rows - 1):
        child = curr_pos.clone().move(0, 1)
        queue.append(child)
        if (child not in parents):
          parents[child] = curr_pos
    
    visited.append(curr_pos)

  path = get_path(start, goal, parents)
  return path
  #return path, explored

def get_path(start, end, parents):
  path = []
  
  current_square = end
  while (current_square != start):
    parent_square = parents[current_square]
    path.insert(0, current_square)
    current_square = parent_square
    
  return path