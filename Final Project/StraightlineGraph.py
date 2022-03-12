from matplotlib import markers
from pyparsing import line
from ast import Return
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


StraightlineGraph()