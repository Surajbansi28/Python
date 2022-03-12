import matplotlib.pyplot as plt
import numpy as np


#main function to generate x and y coordinates of polynomial equation
def polynomailEqGenerator():
    #this will create array containg 10000 numbers from -100 to +100
    x = np.linspace(-100, 100, 10000)
    order = int(input("Enter the order of polynomaial: "))

    #Taking coeffiecient of all terms one by one
    coeffiecients = []
    for i in range(order+1):
        coeffiecent = int(input("Enter coeffiecient of x^{}: ".format(order-i)))
        coeffiecients.append(coeffiecent)

    #Function to return y value corresponding to x value    
    def f(x):
        y = 0
        for i in range(order + 1):
            y += coeffiecients[i]*x**(order-i)
        return y
    #returning list containing two lists: one of x values and other of y values
    return [x, f]

[x, y] = polynomailEqGenerator()
plt.plot(x, y(x))
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
#creating x-axis line
plt.axhline()
#creating y-axis line
plt.axvline()
#limit y-axis values in view
plt.ylim([-100, 100])
 
# giving a title to my graph
plt.title("Polynomial Graph")
plt.show()