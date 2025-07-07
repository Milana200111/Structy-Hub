# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#-----------recursive-------------
# def tree_includes(root, target):
#   if(root is None):
#     return False
#   if(root.val==target):
#     return True 
#   return tree_includes(root.left,target) or tree_includes(root.right,target)
def tree_includes(root, target):
  if(root is None):
    return False 
  stack=[root]
  while(stack):
    node=stack.pop()
    if(node.val==target):
      return True 
    if(node.right):
      stack.append(node.right)
    if(node.left):
      stack.append(node.left)
  return False
      