from cmath import sqrt

print("The Quadratic equation general form is ax^2+bx+c")
a = int(input("Enter the coofficient of x^2:"))
b = int(input("Enter the coofficient of x:"))
c = int(input("Enter the constant:"))

rootsolver = sqrt(((b**2) - 4*a*c))
quadratic1 = (b + rootsolver.real) / (2*a)
quadratic2 = (b - rootsolver.real) / (2*a)
print("x =", quadratic1, "and x =", quadratic2)
