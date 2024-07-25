import numpy as np
from scipy.optimize import fsolve
import time

filename = f"logs/logs.txt"

def log(text):
    with open(filename , 'a') as file:
        T = time.localtime()
        file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")
        
# Fundamental constants
G = 6.6743e-11
k = 9e9

def coll_eqs(p, a, b, c , d):
    x , y = p
    eq1 = a*x + b*y -c
    eq2 = a*x**2 + b*x**2 -d
    sys = (eq1 , eq2)
    return sys

def mag (v):
    # v must be a numpy array
    mag = np.sqrt(v[0]**2 + v[1]**2)
    return mag

# Fundamental forces

def Newtonian_Gravity(G , b1 , b2):
    # Force exerted by m1 on m2
    r = b2.x - b1.x
    #r_dir = r / mag(r)
    F = (-1)*(G * b1.mass * b2.mass) * (r / mag(r)**3)
    return F

def electrostatic(k , b1 , b2):
    # Force extered by q1 on q2
    r = b2.x - b1.x
    #r_dir = r / mag(r)
    F = (k * b1.charge * b2.charge) * (r / mag(r)**3)
    return F 

def collide(p1 , p2):
    if (p1.radius + p2.radius) >= mag(p1.x - p2.x):
        log(f"TIME >> Collision between {p1.name} and {p2.name}")
    else:
        return False
    
    # System of equations: 
    a = p1.mass
    b = p2.mass
        
    c = (p1.mass * mag(p1.v)) + (p2.mass * mag(p2.v))
    d = (p1.mass * mag(p1.v)**2) + (p2.mass * mag(p2.v)**2) ## <-- Need to break into components and solve
        
    initial_guess = (1,1)
        
    start_time = time.time() # Measure time efficiency of Scipy fsolve
    print('!!!!!' , a , b , c, d)
    solution = fsolve(coll_eqs , initial_guess , args = (a,b,c,d)) # Solve system of equations using Scipy fsolve
    end_time = time.time()
    print(f"{solution} in time {end_time - start_time:.4f}")
    
    v1_dir = p1.v / mag(p1.v) # Get directions of both velocity vectors
    v2_dir = p2.v / mag(p2.v)
    
    p1.v = solution[0] * (-1) * v1_dir # Pull magnitude of velocity from fsolve solutions and update velocites in reversed direrction
    p2.v = solution[1] * (-1) * v2_dir # Velocities of bodies updated
    
    return True
        
class body:
    def __init__(self, name, v, x, radius, charge, mass, color):
        self.name = name
        self.v = v
        self.x = x
        self.radius = radius
        self.charge = charge
        self.mass = mass
        self.color = color

        
        
    def net_a(self, b):
        # self is our body of interest
        # calculating net force on self due to b1
        
        collision = collide(self , b)
        
        if collision:
            return 'COLLIDE' # Collision indeed did occur
        else:
            pass

        F_g = Newtonian_Gravity(G , b, self)
        F_c = electrostatic(k, b, self)
        F_net = F_g + F_c # Net force on self
        
        log(f"TIME >> Net force on {self.name} is {F_g} + {F_c} = {F_g + F_c}")
        
        net_a = F_net / self.mass
        
        return net_a


    def update(self, a, del_t):
        # self is our body of interest
        
        del_x = self.v * del_t
        self.x = self.x + del_x
        try:
            del_v = a*del_t
            self.v = self.v + del_v
        except:
            print(f"[ERROR]: {a}")
        
    def update_aftercollide(self , del_t):
        del_x = self.v * del_t
        self.x = self.x + del_x
        

        