n=int(input("enter a the number of terms: "))
n1=0
n2=1
count=0
if(n==1):
 print(n1)
else:
 print("the fibonacci series is: ") 
 while count<n:
  print(n1, end=' ')
  nth=n1+n2
  n1=n2
  n2=nth
  count=count+1