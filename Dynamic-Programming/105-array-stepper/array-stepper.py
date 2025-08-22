def array_stepper(numbers):
  return step(0,numbers,{})
def step(index,numbers,memo):
  if index in memo:
    return memo[index]
  if(index==len(numbers)-1):
    memo[index]=True 
    return True 
  end=numbers[index]+index
  for i in range(index+1,end+1):
    if(step(i,numbers,memo)):
      return True 
  memo[index]=False 
  return False
