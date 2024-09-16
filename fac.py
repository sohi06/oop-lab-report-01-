num=int(input("enter a number: "))
fac=1
if num==0:
  print("the factorial of 0 is 1")
else:
  for i in range(1,num+1):
     fac=fac*i;
  print("the factorial of ",num,"is =",fac)