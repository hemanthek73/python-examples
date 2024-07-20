# factorial=1
# num=int(input("enter teh number:"))
# if num<0:
#   print("factorial does not exist on this number")
# elif num==0:
#   print("factorial of number is :1")
# else:
#   for i in range(1,num+1):
#     factorial=factorial*i
#   print("the factorial of given number ",num," is ",factorial)
def fact(n):
  # if(n==0 or n==1):
  #   return 1
  # else:
  #   return n*fact(n-1)
  return 1 if(n==0 or n==1) else n*fact(n-1)
n=int(input("enter the number:"))
print("the factorial of",n,"is",fact(n))