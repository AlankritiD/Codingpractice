def sumofdigits(n):
  total=0
  while n>0:
    lastdigit=n%10
    total+=lastdigit
    n=n//10
  return total
num=int(input())
print(sumofdigits(num))
