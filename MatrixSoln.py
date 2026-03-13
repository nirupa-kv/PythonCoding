#Builds a matrix based on a list of values and then finds the row with the minimum sum (excluding the first row and first column).
l=[int(x) for x in input("Enter the list: ").split(',')];
n=len(l);
list1=l;
mst=[[0 for x in range(n)] for y in range(n)];
for i in range(n):
   a=1;
   for j in range(i+1,n):
      if(list1[i]!=0):
         mst[i][j]=a;
         list1[i]=list1[i]-1;
         a=a+1;
print(mst);
mini=25;
for i in range(1,n):
   sums=0;
   for j in range(1,n):
      sums=sums+mst[i][j];
   if(sums<mini):
      array=i+1;
      mini=sums;
print(array)
print(mini);