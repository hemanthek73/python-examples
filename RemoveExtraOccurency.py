mylist=["geeks","for","geeks"]
word="geeks"
count=0
n=2
for i in range(0,len(mylist)):
  if(mylist[i]==word):
    count=count+1
    if count==n:
      del mylist[i]
print(mylist)