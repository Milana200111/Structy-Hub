def extra_cable(num_computers, cables):
  roots=[i for i in range(num_computers)]
  size=[1 for i in range(num_computers)]
  for n1,n2 in cables:
    root1=find(roots,n1)
    root2=find(roots,n2)
    if(root1==root2):
      return (n1,n2)
    elif(size[root2]>=size[n1]):
      size[root2]+=size[root1]
      roots[root1]=root2
    else:
      size[root1]+=size[root2]
      roots[root2]=root1
def find(roots,node):
  if(roots[node]==node):
    return node 
  found=find(roots,roots[node])
  roots[node]=found
  return found 
      
  