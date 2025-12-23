from collections import Counter
def most_frequent_char(s):
  dic=Counter(s)
  most_freq=None
  for i in s:
    if(most_freq not in dic or dic[i]>dic[most_freq]):
      most_freq=i
  return most_freq

  