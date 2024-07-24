import physics as p
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

t = np.linspace(0 , 20 , 20*100) 
# initial time, final time, number of frames in between

b1v = np.array([0,0])
b1x = np.array([5,0])
b1 = p.body("b1", b1v, b1x, 1, 0.0005, 1, "blue")

b2v = np.array([0,1])
b2x = np.array([0,0])
b2 = p.body("b2", b2v, b2x, 1, -0.0005, 1, "green")
# name v x radius charge mass color

for i in range(len(t) - 1):

	if i % 100 == 0:
		print(f"> Instance {i}")

	fig , ax = plt.subplots()

	plt.title(f"Time instance {t[i]}")

	ax.set_xlim(-20 , 20)
	ax.set_ylim(-20 , 20)

	circle_b1 = Circle((b1.x[0] , b1.x[1]) , b1.radius , color = b1.color , fill = True)
	circle_b2 = Circle((b2.x[0] , b2.x[1]) , b2.radius , color = b2.color , fill = True)

	ax.add_patch(circle_b1)
	ax.add_patch(circle_b2)

	ax.set_aspect('equal') # Redundant thanks to xlim and ylim

	plt.grid(True)
	plt.show()

	plt.savefig(f"frames/frame_{i}.png")
	plt.close()

	del_t = t[i+1] - t[i]

	net_a_b1 = b1.net_a(b2)
	net_a_b2 = b2.net_a(b1)

	b1.update(net_a_b1 , del_t)
	b2.update(net_a_b2 , del_t)

	# End Loop
