from collections import deque 
def safe_cracking(hints):
  graph={}
  in_degree={i:0 for i in range(10)}
  for n1,n2 in hints:
    if n1 not in graph:
      graph[n1]=[]
    graph[n1].append(n2)
    if n2 not in graph:
      graph[n2]=[]
    in_degree[n2]+=1
  queue=deque([])
  for i in graph:
    if in_degree[i]==0:
      queue.append(i)
  res=[]
  while(queue):
    cur=queue.popleft()
    res.append(str(cur))
    for neighbor in graph[cur]:
      in_degree[neighbor]-=1
      if(in_degree[neighbor]==0):
        queue.append(neighbor)
  return ''.join(res)
    
      
  
      