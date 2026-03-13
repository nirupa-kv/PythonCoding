original_String=input("Enter the string:");
n=len(original_String);   
output=[];                
for i in range(n):        
   comp="";
   for j in range(i,n):   
      if(original_String[j] not in comp):   
         comp+=original_String[j];
      else:
         break
   output.append(comp);                     
length=0;                                   
for x in output:                            
   if(len(x)>length and original_String.find(x)!=-1):
        length=len(x);                               
        final=x;                                     
print("Length of the longest substring with unique characters is ",length);
print("The longest substring without repeating characters is ",final);