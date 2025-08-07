def has_path(graph, src, dst):
  stack=[src]
  while(stack):
    cur=stack.pop()
    if(cur==dst):
      return True
    for neighbor in graph[cur]:
      stack.append(neighbor)
  return False 