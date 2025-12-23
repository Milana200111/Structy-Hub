def fizz_buzz(n):
  pass # todo
  l=[]
  for i in range(1,n+1):
      if i%3==0 and i%5==0:
          l.append('fizzbuzz')
      elif i%5==0:
          l.append('buzz')
      elif i%3==0:
          l.append('fizz')
      else:
          l.append(i)
  return l 