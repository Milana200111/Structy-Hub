class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  new_node=Node(value)
  if(index==0):
    new_node.next=head
    return new_node
  cur=head
  count=0
  while(cur!=None):
    count+=1
    if(count==index):
      next=cur.next
      cur.next=new_node
      new_node.next=next
      return head 
    else:
      cur=cur.next 
    
