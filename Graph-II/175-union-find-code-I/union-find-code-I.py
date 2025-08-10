def count_components(n, edges):
  roots=[i for i in range(n)]
  for n1,n2 in edges:
    root1=find(roots,n1)
    root2=find(roots,n2)
    roots[root2]=root1 
  count=0 
  for i in range(n):
    if(roots[i]==i):
      count+=1
  return count 
    
def find(roots,node):
  if(roots[node]==node):
    return node
  return find(roots,roots[node])
