# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def lowest_common_ancestor(root, val1, val2):
  path_1=find_path(root,val1)
  path_2=find_path(root,val2)
  set_1=set(path_1)
  for i in path_2:
    if i in set_1:
      return i 
def find_path(root,val):
  if root is None:
        return None
  if root.val==val:
        return [root.val]
  left_tree=find_path(root.left,val)
  right_tree=find_path(root.right,val)
  if(left_tree):
        left_tree.append(root.val)
        return left_tree
  if(right_tree):
        right_tree.append(root.val)
        return right_tree
   
      
    
    