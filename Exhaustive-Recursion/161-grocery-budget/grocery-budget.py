def grocery_budget(grocery_list, budget):
  res=[]
  shopping(0,budget,grocery_list,[],res)
  return res 
def shopping(i,budget,grocery_list,cur,res):
  if(i==len(grocery_list)):
    res.append(cur[:])
    return 
  item,cost=grocery_list[i]
  if(budget>=cost):
    cur.append(item)
    shopping(i+1,budget-cost,grocery_list,cur,res)
    cur.pop()
  shopping(i+1,budget,grocery_list,cur,res)