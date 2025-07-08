# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  res=[]
  list=[]
  _all_tree_paths(root,list,res)
  return res 
def _all_tree_paths(root,list,res):
  if root !=None:
    list.append(root.val)
  if(root.left==None and root.right==None):
    res.append(list[::])
    return 
  if(root.left):
    _all_tree_paths(root.left,list,res)
    list.pop()
  if(root.right):
    _all_tree_paths(root.right)
    list.pop()
  
  