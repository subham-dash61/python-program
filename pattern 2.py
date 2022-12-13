a=int(input("enter the number of rows"))
for i in range(a,-1,-1):
    for j in range (0,i+1):
        print("*",end="")
    print("\r")
