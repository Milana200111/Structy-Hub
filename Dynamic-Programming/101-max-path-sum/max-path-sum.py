def max_path_sum(grid):
  tr=len(grid)-1
  tc=len(grid[0])-1
  return maximum(0,0,grid,tr,tc,{})
def maximum(r,c,grid,tr,tc,memo):
  if r==tr and c==tc:
    return grid[r][c]
  if (r,c) in memo:
    return memo[(r,c)]
  row,col=r+1,c+1
  val=-float('inf')
  if(row in range(len(grid))):
    val=max(val,maximum(row,c,grid,tr,tc,memo))
  if(col in range(len(grid[0]))):
    val=max(val,maximum(r,col,grid,tr,tc,memo))
  val+=grid[r][c]
  memo[(r,c)]=val
  return val 
    
