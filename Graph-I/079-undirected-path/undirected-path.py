def undirected_path(edges, node_A, node_B):
  graph={}
  for e1,e2 in edges:
    if e1 not in graph:
      graph[e1]=[]
    graph[e1].append(e2)
    if e2 not in graph:
      graph[e2]=[]
    graph[e2].append(e1)
  stack=[node_A]
  visited=set()
  while(stack):
    cur=stack.pop()
    if cur not in visited:
      visited.add(cur)
      if(cur==node_B):
        return True
      for neighbor in graph[cur]:
        stack.append(neighbor )
  return False 
  
  