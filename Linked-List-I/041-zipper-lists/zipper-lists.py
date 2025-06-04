# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  cur1=head_1
  cur2=head_2
  while(cur1!=None and cur2!=None):
    next=cur1.next
    cur1.next=cur2
    cur2=next
    cur1=cur1.next
  return head_1
  
  
    
