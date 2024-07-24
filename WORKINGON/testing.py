import matplotlib.pyplot as plt
from matplotlib.patches import Circle

import numpy as np

###


fig , ax = plt.subplots()

circle = Circle((1 , 1) , 1 , color = 'red' , fill = True)

ax.add_patch(circle)

ax.set_aspect('equal')

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)


plt.scatter(4 , 4)

plt.grid(True)
plt.show()