# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#---------recursive--------
# def tree_min_value(root):
#   if root is None:
#     return float('inf')
#   return min(root.val,min(tree_min_value(root.left),tree_min_value(root.right)))

#--------iterative----------
def tree_min_value(root):
  minimum=float('inf')
  stack=[root]
  while(stack):
    node=stack.pop()
    minimum=min(minimum,node.val)
    if(node.right):
      stack.append(node.right)
    if(node.left):
      stack.append(node.left)
  return minimum




      
  
