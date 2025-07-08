# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from statistics import mean 
def level_averages(root):
  if root is None:
    return []
  stack=[(root,0)]
  res=[]
  while(stack):
    node,level=stack.pop()
    if(len(res)==level):
      res.append([node.val])
    else:
      res[level].append(node.val)
    if(node.left):
      stack.append((node.left,level+1))
    if(node.right):
      stack.append((node.right,level+1))
  sol=[]
  for i in res:
    sol.append(mean(i))
  return sol 
    
    
  
