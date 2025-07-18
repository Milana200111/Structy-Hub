# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  if(root is None):
    return -float('inf')
  if(root.left==None and root.right==None):
    return root.val
  return root.val+max(max_path_sum(root.left),max_path_sum(root.right))
