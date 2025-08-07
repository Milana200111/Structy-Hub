from collections import deque 
def connected_components_count(graph):
  count=0
  visited=set()
  for edge in graph:
    if edge not in visited:
     count+=component(edge,graph,visited)
  return count 
def component(edge,graph,visited):
  queue=deque([edge])
  visited.add(edge)
  while(queue):
    cur=queue.popleft()
    for neighbor in graph[cur]:
      if neighbor not in visited:
        visited.add(neighbor )
        queue.append(neighbor )
  return 1 