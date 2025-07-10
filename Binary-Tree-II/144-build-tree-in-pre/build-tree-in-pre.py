class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  indices={}
  #create the dict for indices 
  for i in range(len(in_order)):
    val=in_order[i]
    indices[val]=i
  return helper(in_order,pre_order,0,len(in_order)-1,0,len(pre_order)-1,indices)
def helper(in_order,pre_order,start_in,end_in,start_pre,end_pre,indices):
  if(start_in>end_in):
    return None
  value=pre_order[start_pre]
  mid=indices[value]
  root=Node(value)
  left=mid-start_in
  root.left=helper(in_order,pre_order,start_in,mid-1,start_pre+1,start_pre+left)
  root.right=helper(in_order,pre_order,mid+1,end_in,start_pre+left+1,end_pre)
  return root 
  








  