mylist=[1,2,3,4,5,6,7,8,9,0,21,34,67,87,97]
ele=int(input("enter the element to be search in a list:"))
# for i in range(0,len(mylist)):
#   if mylist[i]==ele:
#     print("the element ",ele," found in position",i)
flag=0
for i in mylist:
  if i==ele:
    print("the element ",ele," found in position",i)
    flag=1
if flag==0:
  print("element not found")
