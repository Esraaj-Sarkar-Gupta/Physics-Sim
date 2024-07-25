import os
import time

import physics as phys
import numpy as np


import matplotlib.pyplot as plt
from matplotlib.patches import Circle

filename = f"logs/logs.txt"

START = time.localtime()

try:
    os.remove(filename)
except:
    pass

try:
    os.makedirs('./logs')
    os.makedirs('./frames')
except:
    pass


def log(text):
    with open(filename , 'a') as file:
        T = time.localtime()
        file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")

def log_display(text):
    with open(filename  , 'a') as file:
        T = time.localtime()
        file.write(f"\n (Disp) {T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")
    print(f"{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}")


log_display(f"Logging begins")

t = np.linspace(0, 20, 20*100)
# initial time, final time, number of frames in between

b1v = np.array([+5, 0])
b1x = np.array([0, 0])
b1 = phys.body("b1", b1v, b1x, 1, 0.0005, 5, "blue")

b2v = np.array([-5, 0])
b2x = np.array([5, 0])
b2 = phys.body("b2", b2v, b2x, 1, -0.0005 , 5, "green")
# name v x radius charge mass color

log_display("System characteristics defined and NOT logged")

for i in range(len(t) - 1):
    if i % 100 == 0:
        log_display(f"> Instance {i}")

    fig, ax = plt.subplots()

    plt.title(f"Time instance {t[i]}")

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    circle_b1 = Circle((b1.x[0], b1.x[1]), b1.radius,
                       color=b1.color, fill=True)
    circle_b2 = Circle((b2.x[0], b2.x[1]), b2.radius,
                       color=b2.color, fill=True)

    ax.add_patch(circle_b1)
    ax.add_patch(circle_b2)

    ax.set_aspect('equal')  # Redundant thanks to xlim and ylim

    plt.grid(True)
    plt.show()

    plt.savefig(f"frames/frame_{i}.png")
    plt.close()
    
    log(f"Running instance {t[i+1]} frame {i}. Delta_time = {t[i+1] - t[i]}")
    
    del_t = t[i+1] - t[i]

    net_a_b1 = b1.net_a(b2)
    if type(net_a_b1) == str:
        b1.update_aftercollide(del_t)
    else:
        log(f"[{t[i+1]}] >> [b1] net_a_b1 = {net_a_b1}")
        b1.update(net_a_b1, del_t)
        log(f"[{t[i+1]}] >> Updated b1 -> X: {b1.x} V: {b1.v}")
        
        
    net_a_b2 = b2.net_a(b1)
    if type(net_a_b1) == str:
        b2.update_aftercollide(del_t)
    else:
        log(f"[{t[i+1]}] >> [b2] net_a_b2 = {net_a_b2}")
        b2.update(net_a_b2, del_t)
        log(f"[{t[i+1]}] >> Updated b2 -> X: {b2.x} V: {b2.v}")
        
    log("=====END INSTANCE=====")
    # End Loop
