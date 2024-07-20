arr=[1,4,5,7,8,90,2,654,68,67,3,46,768,73]
max,min=arr[0],arr[0]
n=len(arr)
for i in range(1,n):
  if arr[i]>max:
    max=arr[i]
  if arr[i]<min:
    min=arr[i]
print("the maximum value of this array is:",max)
print("the minimum value of this array is:",min)