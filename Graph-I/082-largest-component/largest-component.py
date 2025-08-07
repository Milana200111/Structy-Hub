from collections import deque 
def largest_component(graph):
  visited=set()
  largest=0
  for edge in graph:
    if edge not in visited:
      visited.add(edge)
      res=count_component(edge,graph,visited)
      largest=max(largest,res)
  return largest 
def count_component(edge,graph,visited):
  queue=deque([edge])
  count=0 
  while(queue):
    cur=queue.popleft()
    count+=1
    for neighbor in graph[cur]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return count 
    
  