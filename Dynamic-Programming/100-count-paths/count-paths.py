def count_paths(grid):
  tr=len(grid)-1
  tc=len(grid[0])-1
  return count(0,0,tr,tc,grid,{})
def count(r,c,tr,tc,grid,memo):
  if (r,c) in memo:
    return memo[(r,c)]
  if(r==tr and c==tc):
    return 1 
  path_count=0 
  row=r+1
  col=c+1
  if row in range(len(grid)) and grid[row][c]!='X':
    path_count+=count(row,c,tr,tc,grid,memo)
  if col in range(len(grid[0])) and grid[r][col]!='X':
    path_count+=count(r,col,tr,tc,grid,memo)
  memo[(r,c)]=path_count
  return path_count
    