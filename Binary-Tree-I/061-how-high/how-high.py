
from collections import deque 
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(node):
  queue=deque([(node,0)])
  while(queue):
    n,h=queue.popleft()
    if(n.left):
      queue.append((n.left,h+1))
    if(n.right):
      queue.append((n.right,h+1))
  return h 
