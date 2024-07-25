import numpy as np
from scipy.optimize import fsolve

def equations(p, a, b, c, d):
  x, y = p
  return (a*x + b*y - c, a*x**2 + b*y**2 - d)

# Example values for a, b, c, d
a, b, c, d = 2, 3, 7, 13

# Initial guess for x and y
initial_guess = (1, 1)  # Adjust initial guess as needed

solution = fsolve(equations, initial_guess, args=(a, b, c, d))
print(solution)