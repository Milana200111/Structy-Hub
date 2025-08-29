# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  prev_val=-1
  count=0
  longest=-float('inf')
  cur=head
  while(cur!=None):
    if(prev_val==-1 or prev_val==cur.val):
      count+=1
    else:
      count=1
    longest=max(longest,count)
    prev_val=cur.val
    cur=cur.next
  return longest
