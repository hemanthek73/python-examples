#----------swapping using temp variable--------
mylst=[1,2,3,4,5,6]
temp=mylst[0]
mylst[0]=mylst[-1]
mylst[-1]=temp
print("swapping using temp variable",mylst)
#----------swapping using * method----------
mylst1=[1,2,3,4,5,6,7,8,9]
start,*mid,end=mylst1
mylst1=[end,*mid,start]
print("The * method swapping:",mylst1)
#--------swapping using pop() ---------------
mylst2=[1,2,3,4,5,6,7,8,9]
first=mylst2.pop(0)
last=mylst2.pop(-1)
mylst2.insert(0,last)
mylst2.append(first)
print("swapping using pop():",mylst2)