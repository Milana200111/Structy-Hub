def can_concat(s, words):
  return can(0,s,words,{})
def can(i,s,words,memo):
  if i==len(s):
    return True
  if i in memo:
    return memo[i]
  for word in words:
    if(s.startswith(word,i)):
      if(can(i+len(word),s,words,memo)):
        memo[i]=True 
        return True
  memo[i]=False 
  return False 
