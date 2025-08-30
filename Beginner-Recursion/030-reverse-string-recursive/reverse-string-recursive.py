def reverse_string(s):
  return reverse(-1,s)

def reverse(idx,s):
  if idx==-(len(s)+1):
    return ''
  return s[idx]+reverse(idx-1,s)
  
