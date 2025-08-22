def counting_change(amount, coins):
  return ways(amount,0,coins,{})
def ways(amount,index,coins,memo):
  if (amount,index) in memo:
    return memo[(amount,index)]
  if amount==0:
    return 1 
  if index>=len(coins):
    return 0 
  count=0 
  coin=coins[index]
  for j in range(0,(amount//coin)+1):
      count+=ways(amount-(coins[index]*j),index+1,coins,memo)
  memo[(amount,index)]=count
  return count 