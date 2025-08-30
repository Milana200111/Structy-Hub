def palindrome(s):
  return palin(0,len(s)-1,s)
def palin(i,j,s):
  if(i>=j):
    return True 
  if(s[i]!=s[j]):
    return False 
  return palin(i+1,j-1,s)