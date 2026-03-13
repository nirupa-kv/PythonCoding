#To check whether brackets in a string are balanced using stacks.
s=input()
n=len(s)
dict={'(':')','{':'}','<':'>','[':']'}
stack1=[]
stack2=[]
flag1=False
for i in s:
   if i in dict.keys():
        stack1.append(i)
        s=s.replace(i,"")
        stack2.append(dict.get(i))
print(stack1)
print(stack2)
print(s)
stack3=list(reversed(stack2))
y=""
for x in s:
   y=stack2.pop()
   print(y)
   if y==x:
      flag1=True
   else:
      flag1=False
      break
print(flag1)
flag2=False
for x in s:
    y=stack3.pop()
    if y==x:
       flag2=True
    else:
       flag2=False
       break
print(flag2)