import heapq
from collections import defaultdict
def lowest_toll(highway_tolls, start_city, end_city):
  graph=defaultdict(list)
  for u,v,w in highway_tolls:
    graph[u].append((v,w))
    graph[v].append((u,w))
  dist={i:float('inf') for i in graph}
  dist[start_city]=0
  heap=[(0,start_city)]
  while(heap):
    d,node=heapq.heappop(heap)
    for neighbor,wt in graph[node]:
      distance=d+wt
      if(distance<dist[neighbor]):
        dist[neighbor]=distance
        heapq.heappush(heap,(distance,neighbor))
  return dist[end_city]
    
  