# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  current=head
  res=[]
  while(current!=None):
    res.append(current.val)
    current=current.next 
  return res 
    
