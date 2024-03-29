import matplotlib.pyplot as plt
import numpy as np

def StraightlineGraph():
# creating an empty list    
    x = []
    y = []

# adding coordinates to the list according to the user
    occurs = int(input("Enter how many coordinates you want to add:"))
    for i in range(0,occurs):
        x.insert(i,input("Enter the x coordinate:"))  
        y.insert(i,input("Enter the y coordinate:")) 
        continue
    
# plotting the points
    plt.plot(x, y, marker ='o')

# naming the x axis
    plt.xlabel('x - axis')
# naming the y axis
    plt.ylabel('y - axis')
 
# giving a title to my graph
    plt.title('Straight Line Graph')
 
# function to show the plot
    plt.show()


def SineFunctionGraph():
# setting the x - coordinates
    u = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
    v = np.sin(u)
 
# plotting the points
    plt.plot(u, v)
# giving a title to sine function graph
    plt.title("Sine Function Graph")
 
# function to show the plot
    plt.show()


def CosineFunctionGraph():
# setting the x - coordinates
    z = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
    v = np.cos(z)
    
# plotting the points
    plt.plot(z, v)
# giving a title to sine function graph
    plt.title("Cosine Function Graph")
    
# function to show the plot
    plt.show()


def quadric_eq():

    # Taking input from the user using coefficients of the equation 
    a=int(input("Enter the coefficient of x^2:"))
    b=int(input("Enter the coeficient of x:"))
    c=int(input("Enter the constant:"))
    x=list(range(-5,5))

    # Axis arrangement
    y=[(a*i**2+b*i+c) for i in x]
    plt.plot(x,y, marker ='o')

    # Plotting the graph 
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Quadric Equation Graph")
   
    plt.show()    


#main function to generate x and y coordinates of polynomial equation
def polynomialEqGenerator():
#this will create array containg 10000 numbers from -100 to +100
    x = np.linspace(-100, 100, 10000)
    order = int(input("Enter the order of polynomial: "))

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

#Creating a function to be recalled
def PolynomialCaller():
    [x, y] = polynomialEqGenerator()
    plt.plot(x, y(x))
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    #creating x-axis line
    plt.axhline()
    #creating y-axis line
    plt.axvline()
    # giving a title to the graph
    plt.title("Polynomial Graph")
    plt.show()


def Exponential_Curve(value):
    value = np.arange(-2,4,0.001)
    # we can write any value it only amplifies
    amplitude = np.exp(value)
    plt.plot(value,amplitude)
    # naming The axis
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    # title of the graph
    plt.title('Exponential Graph')
    plt.grid()
    plt.show()
    

# Developers of the program
print("Welcome to the Python Graph Plotting Program!")
print("Developed by : Shahzeb Abro, Mustafa Sheikh, Syed Sumam, M.Umair, Rohan Ahmed and M.Abdul Rafay")

# Menu Interface
print("Press the key 1. If you want to plot a Straight line Graph:")
print("Press the key 2. If you want to plot a Quadratic Equation Graph:")
print("Press the key 3. If you want to plot a Polynomial Equation Graph:")
print("Press the key 4. If you want to plot an Exponential Graph:")
print("Press the key 5. If you want to plot a Sine Function Graph:")
print("Press the key 6. If you want to plot a Cosine Function Graph:")
print("Press the key 7. If you want to exit the Program:")

# Creating an actual menu for graph plotting program
def menu():
    choice = int(input("Please enter your desired key:"))
# Making choice according to the prompt
    if choice == 1:
        StraightlineGraph()
    if choice == 2:
        quadric_eq()
    if choice == 3:
        PolynomialCaller()
    if choice == 4:
        Exponential_Curve(1)
    if choice == 5:
        SineFunctionGraph()
    if choice == 6:
        CosineFunctionGraph()
    if choice == 7:
        pass      

# Executing the menu in the code
menu()

while True:

# Using user's input to decide to either execute the program or not
    print("Do you want to continue using the Program?")
    print("Press 1 to Continue:")
    print("Press 2 to Exit:")
    consideration = int(input("Enter your choice:"))
    if consideration == 1:
        menu()
    else:  
        print("Thank you for Using Our Program!")
        break

