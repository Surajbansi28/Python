
import matplotlib.pyplot as plt
def quadric_eq(a,b,c):
    x=list(range(-5,5))
    y=[(a*i**2+b*i+c) for i in x]
    plt.plot(x,y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Quadric Equation Graph")
a=int(input("Enter any number:"))
b=int(input("Enter any number:"))
c=int(input("Enter any number:"))
quadric_eq(a,b,c)
plt.show()    