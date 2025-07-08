# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
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
  for i in range(len(res)):
    res[i]=sum(res[i])/len(res[i])
  return res 
    
    
  
