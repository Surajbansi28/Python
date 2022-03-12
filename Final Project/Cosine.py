import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,20)
plt.plot(np.cos(x),color='g',linewidth=2,label='Cosine Curve')
#Adding Axix Labwls
plt.xlabel('Time')
plt.ylabel('Amplitude')
#Adding Title
plt.title('Cosine Curve')
#Adding Legend
plt.legend()
#Adding GridLines
plt.grid()
plt.show()
             
