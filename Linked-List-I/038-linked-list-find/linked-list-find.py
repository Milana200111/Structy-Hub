# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  if head==None:
    return False
  if(head.val==target):
    return True 
  return linked_list_find(head.next,target)
  # cur=head
  # while(cur!=None):
  #   if(cur.val==target):
  #     return True 
  #   cur=cur.next
  # return False 
