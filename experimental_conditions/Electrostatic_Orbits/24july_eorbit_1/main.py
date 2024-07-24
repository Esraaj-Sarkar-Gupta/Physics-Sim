import physics as p
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0 , 200 , 200*10) 
# initial time, final time, number of frames in between

b1v = np.array([0,1.73205])
b1x = np.array([3,0])
b1 = p.body("b1", b1v, b1x, 1, 1e-6, 1, "blue")

b2v = np.array([0,0])
b2x = np.array([0,0])
b2 = p.body("b2", b2v, b2x, 1, -1e-3, 1, "green")

# name v x radius charge mass color

for i in range(len(t)-1):
    
    if i % 100 == 0:
        print(f"> Instance {i}")
    
    plt.figure()
    plt.title(f"Time instance {t[i]}")
    plt.xlim(-10 , 10)
    plt.ylim(-10 , 10)

    plt.scatter(b1.x[0] , b1.x[1] , color = b1.color)
    plt.scatter(b2.x[0] , b2.x[1] , color = b2.color)

    del_t = t[i+1] - t[i]
    net_a_b1 = b1.net_a(b2)
    b1.update(net_a_b1, del_t)
    
    if b1.v[0] > 1e5 or b1.v[1] > 1e5:
        print(f'[!!] Extreme: {b1.v}')

    plt.grid(True)
    # plt.show()
    plt.savefig(f"frames/frame_{i}.png")
    plt.close()
