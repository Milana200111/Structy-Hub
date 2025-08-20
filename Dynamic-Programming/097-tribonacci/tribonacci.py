def tribonacci(n):
  return tribo(n,{})
def tribo(n,memo):
  if n==0 or n==1:
    return 0 
  if n==2:
    return 1
  if n in memo:
    return memo[n]
  memo[n]=tribo(n-1,memo)+tribo(n-2,memo)+tribo(n-3,memo)
  return memo[n]