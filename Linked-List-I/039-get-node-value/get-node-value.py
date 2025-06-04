# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  cur=head
  cur_index=0
  while(cur!=None):
    if(index==cur_index):
      return cur.val
    cur=cur.next
    cur_index+=1
  return None 
  
    
