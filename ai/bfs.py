def bfs(start, goal, visited, grid):
  queue = [start]
  parents = {} # keep track of node parents
  
  while queue:
    pos = queue.pop(0)

    # Goal check
    if (pos == goal):
      return parents
    
    elif (pos not in visited):
      visited[pos] = True

      # Add children to the bfs queue
      children = grid.get_children(pos)
      for child in children:
        queue.append(child)

        # Register parents to construct a path later on
        if (child not in parents):
          parents[child] = pos
