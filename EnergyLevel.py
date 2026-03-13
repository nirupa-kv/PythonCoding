#Energy accumulation problem: 
#Determine when the energy becomes negative, then compute how much the previous value should be increased to keep the energy positive.
array=[int(x) for x in input("Enter the elements of the array: ").split(',')]
energy=0
initial=0
prev=0
for x in array:
   energy=energy+x
   print("Energy: ",energy)
   if energy<0:
      initial=(energy*-1)+prev+1
      print("The value of ",prev,"should be modified as ",initial)
      energy=1
   prev=x
