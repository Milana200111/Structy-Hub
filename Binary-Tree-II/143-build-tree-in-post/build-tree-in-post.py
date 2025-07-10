class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  return _build_tree_in_post(in_order,post_order,0,len(in_order)-1,0,len(post_order)-1)
def _build_tree_in_post(in_order,post_order,start_in,end_in,start_post,end_post):
  if(start_in>end_in):
    return None
  val=post_order[end_post]
  root=Node(val)
  mid=in_order.index(val)
  left=mid-start_in
  root.left=_build_tree_in_post(in_order,post_order,start_in,mid-1,start_post,start_post+left-1)
  root.right=_build_tree_in_post(in_order,post_order,mid+1,end_in,start_post+left,end_post-1)
  return root 







  