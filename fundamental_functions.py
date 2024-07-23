print('> Start')
import numpy as np
import time as tm
import matplotlib as mpl

plt = mpl.pyplot

print("Imports completed")

# Fundamental constants of nature:

G = 6.6743e-11
k = 9e9


def mag (v):
    # v must be a numpy array
    mag = np.sqrt(v[0]**2 + v[1]**2)
    return mag
    
def Newtonian_Gravity(G , m1, m2 , r1 , r2):
    # Force exerted by m1 on m2
    r = r2 - r1
    #r_dir = r / mag(r)
    
    F = (G * m1 * m2) * (r / mag(r)**3)
    
    return F

def electrostatic(k , q1 , q2 , r1 , r2):
    # Force extered by q1 on q2
    r = r2 - r1
    #r_dir = r / mag(r)
    
    F = (-1) * (k * q1 * q2) * (r / mag(r)**3)
    
    return F


m1 = 5e5
m2 = 10e5

q1 = 5e-5
q2 = 5e-5



r1 = np.array([0,0])
r2 = np.array([5,5])

FG = Newtonian_Gravity(G, m1, m2, r1, r2)
FE = electrostatic(k, q1, q2, r1, r2)

XG = [r1[0] , FG[0]]
YG = [r1[1] , FG[1]]

XE = [r1[0] , FE[0]]
YE = [r1[1] , FE[1]]

print(XG ,'\n' , YG)
print("===")
print(XE , '\n' ,  YE)

plt.figure()
plt.scatter(r1[0] , r1[1] , color = 'green')
plt.scatter(r2[0] , r2[1] , color = 'blue')

plt.plot(XG , YG , color = 'red')
plt.scatter(FG[0] , FG[1] , color = 'red')

plt.title("Gravity")
plt.show()

plt.figure()
plt.title("Electrostatic")

plt.scatter(r1[0] , r1[1] , color = 'green') # mass 1
plt.scatter(r2[0] , r2[1] , color = 'blue') # mass 2

plt.plot(XE , YE , color = 'purple')
plt.scatter(FE[0] , FE[1] , color = 'purple')

plt.show()
print("> End")