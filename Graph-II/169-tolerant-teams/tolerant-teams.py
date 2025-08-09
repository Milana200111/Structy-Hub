from collections import deque 
def tolerant_teams(rivalries):
  graph={}
  for n1,n2 in rivalries:
    if n1 not in graph:
      graph[n1]=[]
    graph[n1].append(n2)
    if n2 not in graph:
      graph[n2]=[]
    graph[n2].append(n1)
  colour_dict={}
  for node in graph:
    if node not in colour_dict:
      if(not colour(node,graph,colour_dict)):
        return False
  return True 
def colour(node,graph,colour_dict):
  queue=deque([(node,'red')])
  colour_dict[node]='red'
  while(queue):
    node,color=queue.popleft()
    if(color=='red'):
      neighbor_color='blue'
    else:
      neighbor_color='red'
    for neighbor in graph[node]:
      if neighbor not in colour_dict:
        colour_dict[neighbor]=neighbor_color
        queue.append((neighbor,neighbor_color))
      else:
        if(colour_dict[neighbor]!=neighbor_color):
         return False 
  return True 
    
    