num=int(input("enetr the range for fib number:"))
fib=[]
for i in range(0,num+1):
  if i==0:
    fib.append(0)
  elif i==1:
    fib.append(1)
  else:
    fib1=fib[-2]+fib[-1]
    fib.append(fib1)
print(fib)