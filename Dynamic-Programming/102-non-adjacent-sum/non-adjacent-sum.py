def non_adjacent_sum(nums):
  return sum(0,nums,{})
def sum(index,nums,memo):
  if(index>=len(nums)):
    return 0 
  if index in memo:
    return memo[index]
  val=max(nums[index]+sum(index+2,nums,memo),sum(index+1,nums,memo))
  memo[index]=val
  return val 
  