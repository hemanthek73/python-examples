num=int(input("enter the num: "))
count=0
if(num>1):
  for i in range(1,num+1):
    if num%2==0:
      count=count+1
  if count==2:
    print("the number is prime")
  else:
    print("the number is not a prime")

