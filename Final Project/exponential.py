import matplotlib.pyplot as plt
import numpy as np

value= np.arange(-2,4,0.001)
# we can write any value it only amplifies
amplitude = np.exp(value)
plt.plot(value,amplitude)
# naming The axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# title of the graph
plt.title('Exopnential Graph')
plt.grid()
plt.show()
