a=input("enter a string")
c=0
for i in range(0, int(len(a)/2)):
    if (a[i]!= a[len(a)-i-1]):
        c=c+1
      
 
if (c>0):
    print("not palindrome")
else:
    print("palindrome")

