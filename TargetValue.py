'''The program searches for a target value in an array.
If the element exists, it prints the first index.
If it does not exist, it finds the position where the element can be inserted.
'''
array=[int(x) for x in input("Enter the elements of the array: ").split(',')];
target=int(input("Enter the target value: "))
if target in array:
   print("Element found first at index ",array.index(target))
else:
   mini=[x for x in array if x<target]
   maxi=[y for y in array if y>target]
   print(mini)
   print(maxi)
   if len(maxi)==0 and len(mini)!=0:
      minvalue=max(mini)
      if(array.index(minvalue)==0):
         value=array.index(minvalue)
      value=array.index(minvalue)+1
   elif len(mini)==0 and len(maxi)!=0:
      maxvalue=min(maxi)
      if(array.index(maxvalue)==0):
         value=array.index(maxvalue)
      value=array.index(maxvalue)
   else:
      minvalue=max(mini)
      value=array.index(minvalue)+1
   print("Element not found! Can be inserted at ",value)
