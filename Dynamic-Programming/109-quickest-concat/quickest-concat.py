def quickest_concat(s, words):
  c=can(0,s,words,{})
  return -1 if(c==float('inf')) else c

def can(i,s,words,memo):
  if i in memo:
    return memo[i]
  if i==len(s):
    return 0 
  count=float('inf')
  for word in words:
    if(s.startswith(word,i)):
      res=1+min(count,can(i+len(word),s,words))
      count=min(res,count)
      memo[i]=count
  return count 