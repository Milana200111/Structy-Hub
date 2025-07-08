# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  if root is None:
    return []
  stack=[root]
  res=[]
  while(stack):
    node=stack.pop()
    if(node.left== None and node.right==None):
      res.append(node.val)
    if(node.right):
      stack.append(node.right)
    if(node.left):
      stack.append(node.left)
  return res 
      
  
