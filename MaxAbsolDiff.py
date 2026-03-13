#To find the maximum absolute difference between adjacent numbers after sortingnums=input()
nums=[int(x) for x in input("Enter numbers separated by space: ").split(',')]
n=len(nums)
min=0
swap=0
nums.sort()
print(nums)
listcomp=[nums[i]-nums[i+1] for i in range(0,n-1)]
for i in range(0,n-1):
   if listcomp[i]<0:
      listcomp[i]=listcomp[i]*(-1)
print(listcomp)
if n>1:
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if nums[min]>nums[j]:
                min=j
        swap=nums[i]
        nums[i]=nums[min]
        nums[min]=swap
    print(nums)
    diff=[]
    val=0
    for i in range(0,n-1):
       val=nums[i]-nums[i+1]
       if val>0:
          diff.append(val)
       else:
          val=val*(-1)
       diff.append(val)
    print(diff)
    final=max(diff)
else:
    final=0
print(final)