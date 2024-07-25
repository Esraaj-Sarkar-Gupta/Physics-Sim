import numpy as np

# Fundamental constants
G = 6.6743e-11
k = 9e9

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

class body:
    def __init__(self, name, v, x, radius, charge, mass, color):
        self.name = name
        self.v = v
        self.x = x
        self.radius = radius
        self.charge = charge
        self.mass = mass
        self.color = color


    def net_a(self, b1):
        # self is our body of interest
        # calculating net force on self due to b1

        F_g = Newtonian_Gravity(G , b1, self)
        F_c = electrostatic(k, b1, self)
        F_net = F_g + F_c # Net force on b2
        net_a = F_net / self.mass
        
        return net_a


    def update(self, a, del_t):
        # b2 is our body of interest

        #del_x = (self.v * del_t) + (0.5 * a + (del_t ** 2))
        #self.x = self.x + del_x

        del_x = self.v * del_t
        self.x = self.x + del_x
        
        del_v = a*del_t
        self.v = self.v + del_v
