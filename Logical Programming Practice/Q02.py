a = [1,2,3,4,5,6]
ub = len(a)-1
n = int(input("Enter the Rotation Range:"))
for i in range(0,n):
    b = a[0]
    for j in range(0,ub):
        a[j] =a[j+1]
    a[ub] = b
for i in range(0,len(a)):
    print(a[i])
    