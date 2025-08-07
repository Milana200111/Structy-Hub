from collections import deque 
def shortest_path(edges, node_A, node_B):
  graph={}
  for n1,n2 in edges:
    if n1 not in graph:
      graph[n1]=[]
    graph[n1].append(n2)
    if n2 not in graph:
      graph[n2]=[]
    graph[n2].append(n1)
  visited=set(node_A)
  queue=deque([(node_A,0)])
  while(queue):
    node,distance=queue.popleft()
    if(node==node_B):
      return distance
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor,distance+1))
  return -1 
    
  