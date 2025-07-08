# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):
  if root is None:
    return []
  res=[]
  stack=[(root,0)]
  while(stack):
    node,level=stack.pop()
    if(len(res)==level):
       res.append([node.val])
    else:
      res[level].append(node.val)
     
    if(node.right):
      stack.append((node.right,level+1))
    if(node.left):
      stack.append((node.left,level+1))
  return res 