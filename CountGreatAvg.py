#To find how many elements in the array are greater than the average of all previous elements
arr=[int(x) for x in input("Enter the array elements: ").split(',')]
count=0
print(arr)
avg=0
for i in range(0,len(arr)):
   if(i>0):
      arr1=arr[0:i]
      print("Array:")
      print(arr1)
      avg=float(sum(arr1)/len(arr1))
      print("Average:")
      print(avg)
      if(avg<float(arr[i])):
         print(arr[i],">",avg)
         count=count+1
      print("Count value:",count)
      arr1=[]
      print("\n")
print("Count:",count)
'''
arr = [int(x) for x in raw_input("Enter the array elements (comma-separated): ").split(',')]
count = len([x for i, x in enumerate(arr) if i > 0 and x > (sum(arr[:i]) / i)])
print("Array:", arr)
print("Count:", count)
'''