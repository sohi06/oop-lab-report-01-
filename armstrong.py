x= int(input("enter a number: "))
a=str(x)
l=len(a)
c=0
for i in a:
 i=int(i)
 c=c+i**l
print(c) 
if (c==x):
 print(f"{x} is an armstrong number.")
else: 
 print(f"{x} is not an armstrong number.")

   