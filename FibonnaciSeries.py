def fibo(n):
  a,b=0,1
  fibseq=[]
  for i in range(n):
    fibseq.append(a)
    a,b=b,a+b
  return fibseq
num=10
print(fibo(num))
