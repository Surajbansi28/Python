import array as arr
z = int(input("Enter the number of values you want to input:"))
a= int(input("Enter the number of rows you want to create:"))
b = int(input("Enter the number of Coloumns you want to create:"))
c = int(input("Enter the depth you want in your array:"))
arr = [[[0]*b]*a]*c
for i in range(0, z):
    q = print("Do you want to Continue(True/False)?:")
    u = bool(input())
    flag = True
    if u == flag:
        r = int(input("Enter the radius from the origin:"))
        theta = int(input("Enter the angle from the initial meridian plane:"))
        phy = int(input("Enter the Angle from polar Axis:"))
        for k in range(0,c):
            for i in range(0,a):
                for j in range(0,b):
                    arr[k][j][i] = r , theta , phy 
                    print( "(r, Theta, Phy) = " , arr[k][j][i], end=',')
                    print('\n')
    else:
        if u != flag:
            break
            



