def province_sizes(n, roads):
  size=[1 for i in range(n)]
  roots=[i for i in range(n)]
  for n1,n2 in roads:
    root1=find(roots,n1)
    root2=find(roots,n2)
    if(root1!=root2):
      if(size[root1]>=size[root2]):
        roots[root2]=root1
        size[root1]+=size[root2]
      else:
        roots[root1]=root2
        size[root2]+=size[root1]
  res=[]
  for i in range(n):
    if(roots[i]==i):
      res.append(size[i])
  return res  
def find(roots,node):
  if(roots[node]==node):
    return node
  found=find(roots,roots[node])
  roots[node]=found
  return found 
        
  