def count_compounds(compound, elements):
  return count_ways(0,compound,elements,{})
def count_ways(i,compound,elements,memo):
  if i in memo:
    return memo[i]
  if i ==len(compound):
    return 1 
  ways=0 
  for word in elements:
    ele=word.lower()
    if(compound.startswith(ele,i)):
      ways+=count_ways(i+len(ele),compound,elements,memo)
  memo[i]=ways
  return ways
