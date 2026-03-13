#To count how many times the value k appears either:
#Directly in the list, and
#As a prefix sum of the list.
nums=list(input("Enter the list: ").split(','))
k=int(input("Enter a number: "))
count=0
n=len(nums)
if k in nums:
    count=count+1
lists=[]
val=0
for i in range(0,n-1):
    val=val+int(nums[i])
    lists.append(val)
print(lists)
for m in range(0,len(lists)):
    if lists[m]==k:
        count=count+1
print(count)