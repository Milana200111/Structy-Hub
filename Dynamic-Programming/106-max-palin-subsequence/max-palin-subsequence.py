def max_palin_subsequence(string):
  return palin(0,len(string)-1,string,{})
def palin(i,j,string,memo):
  if(i==j):
    return 1
  if(i>j):
    return 0 
  if (i,j) in memo:
    return memo[(i,j)]
  l=0
  if(string[i]==string[j]):
    l+=2+palin(i+1,j-1,string,memo)
  else:
    l+=max(palin(i,j-1,string,memo),palin(i+1,j,string,memo))
  memo[(i,j)]=l
  return l 
