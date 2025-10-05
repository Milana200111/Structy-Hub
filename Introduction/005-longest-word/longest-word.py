def longest_word(sentence):
  longest=''
  for i in sentence.split():
    if len(i)>=len(longest[-1]):
      longest.append(i)
  return longest[-1]