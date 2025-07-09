# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def is_binary_search_tree(root):
  res=[]
  _is_binary_search_tree(root,res)
  for i in range(len(res)-1):
    j=i+1
    if(res[i]>res[j]):
      return False
  return True 
def _is_binary_search_tree(root,res):
  if(root.left):
    _is_binary_search_tree(root.left,res)
  res.append(root.val)
  if(root.right):
    _is_binary_search_tree(root.right,res)
  