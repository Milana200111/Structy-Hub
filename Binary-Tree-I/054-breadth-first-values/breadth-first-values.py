from collections import deque 
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
  queue=deque([root])
  res=[]
  while(queue):
    node=queue.popleft()
    
  
