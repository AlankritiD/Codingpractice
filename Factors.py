def findfactors(n):
  facts=[]
  for i in range(1,n+1):
    if n%i==0:
      facts.append(i)
  return facts
num=89
print(findfactors(num))
