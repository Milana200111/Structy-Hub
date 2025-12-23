from collections import Counter
def most_frequent_char(s):
  seen=set()
  d=Counter(s)
  most_freq=''
  higest=0
  for i in s:
    if i not in seen:
      if d[i]>higest:
        higest=d[i]
        most_freq=i
        seen.add(i)
  return most_freq

  