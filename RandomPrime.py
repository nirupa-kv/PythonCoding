#Generates random numbers, separates prime numbers, and then calculates percentages.
import random;
import math;
n=int(input("Enter the number of elements:"));
initial_list=list();
list2=list();
list1=[];
for i in range(n):
   initial_list.append(random.randint(1,100));
print("Source:",initial_list);
list1=list(set(initial_list));
for x in list1:
   flag=0;
   for i in range(2,int(math.sqrt(x)+1)):
      if((x%i==0 and x!=i) or x==1):
         flag=1;
         break;
   if(flag==0):
      list1.remove(x);
      list2.append(x);
print("Filtered Source list:",list1);
print("Prime numbers list:",list2);
print("Percentage of Filtered Source list:",(len(list1)*100)/n);
print("Percentage of Prime numbers list:",(len(list2)*100)/n);
