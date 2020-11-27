x=int(input("Enter the value of X "))
y=int(input("Enter the value of Y "))
z=int(input("Enter the value of Z "))
e=y%x
val=e+z
if x>0 and y>0 and z>0:
    if val<x:
        print("NO")
    else:
        print("YES")
else:
    print("valid entry required")
