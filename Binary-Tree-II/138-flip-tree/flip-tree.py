# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  if root is None:
    return None
  right=flip_tree(root.left)
  left=flip_tree(root.right)
  root.right=right
  root.left=left
  return root 