# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root):
  res=[]
  _post_order(root,res)
  return res 
def _post_order(root,res):
  if root is None:
    return 
  if(root.left):
    _post_order(root.left,res)
  if(root.right):
    _post_order(root.right,res)
  res.append(root.val)