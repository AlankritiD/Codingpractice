def fetchdupes(arr):
  duplicates=[]
  seen=set()
  for i in arr:
    if i in seen:
      duplicates.append(i)
    else:
      seen.add(i)
  return duplicates
array=list(map(int,input("enter:").split()))
print(fetchdupes(array))
