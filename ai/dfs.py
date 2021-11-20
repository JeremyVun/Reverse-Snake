
def dfs(start, goal, visited, grid): 
  stack = [start]
  parents = {} # keep track of node parents

  while stack:
    pos = stack.pop(-1)

    # Goal check
    if pos == goal:
      return parents

    # Search deeper using a stack
    elif pos not in visited:      
      visited[pos] = True

      children = grid.get_children(pos)
      for child in children:
        if child not in visited:
          stack.append(child)

          # Record the node parent so we can construct a path later on
          if child not in parents:
            parents[child] = pos
