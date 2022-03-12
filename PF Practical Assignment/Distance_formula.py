from cmath import sqrt

x1 = int(input("Enter the first x-coordinate:"))
x2 = int(input("Enter the second x-coordinate:"))
y1 = int(input("Enter the first y-coordinate:"))
y2 = int(input("Enter the second y-coordinate:"))

distance = sqrt(((y2 - y1)**2) + ((x2 - x1)**2))
print("The distance between the two points is:" , distance.real)