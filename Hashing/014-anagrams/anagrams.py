from collections import Counter
def anagrams(s1, s2):
  l=Counter(s1)
  t=Counter(s2)
  if(l==t):
    return True
  return False
  