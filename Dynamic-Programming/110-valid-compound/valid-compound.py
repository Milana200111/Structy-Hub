def valid_compound(compound, elements):
  return is_valid(0,compound,elements,{})
def is_valid(i,compound,elements,memo):
  if i in memo:
    return memo[i]
  if i==len(compound):
    return True 
  for ele in elements:
    if(compound.startswith(ele.lower(),i)):
      if(is_valid(i+len(ele),compound,elements,memo)):
        memo[i]=True 
        return True 
  memo[i]=False 
  return False 
      
    
