def min_change(amount, coins):
  ans=minimum(amount,coins,{})
  if(ans==float('inf')):
    return -1
  else:
    return ans

def minimum(amount,coins,memo):
  if amount in memo:
    return memo[amount]
  if amount==0:
    return 0 
  min_coins=float('inf')
  for i in coins:
    if(amount>=i):
      res=1+minimum(amount-i,coins,memo)
      min_coins=min(min_coins,res)
  memo[amount]=min_coins
  return min_coins
