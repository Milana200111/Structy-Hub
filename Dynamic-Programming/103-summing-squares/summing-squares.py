def summing_squares(n):
  return sum(n,{})
def sum(n,memo):
  if n==0:
    return 0 
  min_count=float('inf')
  for i in range(1,n+1):
    if(i*i>n):
      break 
    else:
      val=1+sum(n-(i*i),memo)
      min_count=min(min_count,val)
  memo[n]=min_count
  return min_count
      
