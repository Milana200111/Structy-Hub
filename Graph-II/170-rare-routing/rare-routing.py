from collections import deque 
def rare_routing(n, roads):
  if not roads:
    return False 
  graph={}
  for n1,n2 in roads:
    if n1 not in graph:
      graph[n1]=[]
    graph[n1].append(n2)
    if n2 not in graph:
      graph[n2]=[]
    graph[n2].append(n1)
  visited=set()
  comp_count=[0]
  for node in graph:
    if node not in visited:
      if(detect_cycle(node,graph,visited,comp_count)==True or comp_count[-1]>1):
        return False
  return True 
def detect_cycle(node,graph,visited,comp_count):
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
  comp_count[-1]+=1
  return False 
        








    
  