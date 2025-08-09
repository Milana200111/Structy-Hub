from collections import deque 
def rare_routing(n, roads):
  if not roads:
    return False 
  graph={i:[] for i in range(n)}
  for n1,n2 in roads:
    graph[n1].append(n2)
    graph[n2].append(n1)
  visited=set()
  comp_count=0
  for node in graph:
    if node not in visited:
      if(detect_cycle(node,graph,visited)):
        return False
      comp_count+=1
      if(comp_count>1):
        return False 
  return True 
def detect_cycle(node,graph,visited):
  queue=deque([(node,-1)])
  visited.add(node)
  while(queue):
    current,parent=queue.popleft()
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append((neighbor,current))
        visited.add(neighbor)
      elif(neighbor!=parent):
        return True 
  return False 
        








    
  