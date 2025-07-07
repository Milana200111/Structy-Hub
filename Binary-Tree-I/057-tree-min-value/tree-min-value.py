# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  if root is None:
    return float('inf')
  return min(root.val,min(tree_min_value(root.left),tree_min_value(root.right)))