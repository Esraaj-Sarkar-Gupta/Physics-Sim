import os
import time

import physics as phys
import numpy as np


import matplotlib.pyplot as plt
from matplotlib.patches import Circle

filename = f"logs/logs.txt" # Temporary filename that the log file is opened with

START = time.localtime() # Pulls the start time of the script as localtime

savename = f"logs/logs_{START[7]}_{START[3]}-{START[4]}-{START[5]}.txt" # Filename that the log file is finally saved with 

try:
    os.remove(filename) # Any older files with the same filename will be deleted
except:
    pass

try:
    os.makedirs('./logs') # Ensures logging directory and frames directory are present, essential for obtaining data from the script
    os.makedirs('./frames')
except:
    pass


def log(text):
    with open(filename , 'a') as file:
        T = time.localtime()
        file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n") # Writes log into the log file in special format

def log_display(text):
    with open(filename  , 'a') as file:
        T = time.localtime()
        file.write(f"\n(Disp) {T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n") # Writes log into the log file in special format
    print(f"{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}") # Prints log into the output console in special format


log_display(f"Logging begins")

total_sim_time = 20 # Total seconds simulated
sim_resolution = 100 # Frames per simulated second

t = np.linspace(0, total_sim_time , total_sim_time * sim_resolution)
# initial time, final time, number of frames in between

#Defining the system:
b1v = np.array([2, 2])
b1x = np.array([0, 0])
b1 = phys.body("b1", b1v, b1x, 0.5, 0.0, 5, "blue")

b2v = np.array([0, 0])
b2x = np.array([1, 1])
b2 = phys.body("b2", b2v, b2x, 0.5, 0.0, 5, "green")

b3v = np.array([0, 0])
b3x = np.array([3, 3])
b3 = phys.body("b3", b3v, b3x, 0.5, 0.0, 5, "red")

b4v = np.array([-1, -1])
b4x = np.array([-2, -2])
b4 = phys.body("b4", b4v, b4x, 0.5, 0.0, 5, "yellow")

b5v = np.array([0.5 , 0.5])
b5x = np.array([-4, -4])
b5 = phys.body("b5", b5v, b5x, 0.5, 0.0, 5, "purple")


# Format: name v x radius charge mass color

system = [b1 , b2 , b3 ,b4] # Storing the system in a list

log_display("System characteristics defined and NOT logged")

start_time = time.time() # Note start time of the loop to compute CPU runtime
for i in range(len(t) - 1):
    
    if i % 100 == 0:
        log_display(f"Instance {i}/{total_sim_time * sim_resolution}") # Progress logging
        

    fig, ax = plt.subplots() # Open plot (frame)

    plt.title(f"Time instance {t[i]}") # Title the plot

    ax.set_xlim(-20, 20) # Plot dimensions
    ax.set_ylim(-20, 20)
    
    circles = [] # List to store plot patches (circles) for each element in the system
    
    for body in system: # Define patches (circles) for each element (body) in the system with corresponding properties
        circles.append(Circle((body.x[0] , body.x[1]) , body.radius , color = body.color , fill = True)) 
        
    for patch in circles:
        ax.add_patch(patch) # Add all the patches (circles) to the plot

    ax.set_aspect('equal')  # Redundant thanks to xlim and ylim

    plt.grid(True)
    #plt.show() # Displays plot in the terminal

    plt.savefig(f"frames/frame_{i}.png") # Saves the plot into the frames directory if plt.show() is removed
    plt.close()
    
    log("=====START INSTANCE=====")
    log(f"Running instance {t[i+1]} frame {i}. Delta_time = {t[i+1] - t[i]}")
    
    del_t = t[i+1] - t[i] # Determine time interval used to compute results of the Gallilean transforms
    
    system_acc = [] # Holds the values of acceleration for each element in the system
    system_collision =[] # Holds the boolean value of a collision (true / false) for each element in the system
    for index in range(len(system)):
        system_acc.append(np.array([0,0])) # Zero vector (to be used as a base for addition of computed acceleration vectors)
        system_collision.append(False) # Sets default collision boolean to False for each element in system_collision
    
    for index in range(len(system)):
        main_body = system[index] # Selects main body (body of interest)
        log(f"[{t[i+1]}] - {i} >> Computing system element {main_body.name}")
        
        for second_index in range(len(system)): # Main body is matched with every other body in the system, Selects secondary body
            second_body = system[second_index]
            if main_body == second_body: # Prevents main body from being matched with itself
                system_acc[index] = system_acc[index] + np.array([0,0]) 
            else:
                acc = main_body.net_a(second_body) # Computes acceleration of main body due to the effects of the secondary body
                log(f"[{t[i+1]}] - {i} >> Computing system element {main_body.name} with {second_body.name}, acceleration = {acc}")
                if type(acc) == str: # acc = 'COLLISON' if function net_a() detects a collision
                    system_collision[index] = True # Checks for collision and changes the collision boolean value to True if collision is deteced
                else:
                    system_acc[index] = system_acc[index] + acc # Acceleration is added to the total acceleration if no collision is detected
    
    for index in range(len(system)): # Iterates through every body (element) in the system
        if system_collision[index]: # Checks if body chosen is undergoing a collision
            system[index].update_aftercollide(del_t) # Runs appropriate update function
        else:
            system[index].update(system_acc[index], del_t) # Runs regular update() function
   
        
    log("=====END INSTANCE=====")
    log("[HouseKeeper]: System State:")
    for j in range(len(system)):
        log(f"{system[j].name}: X = {system[j].x} ; V = {system[j].v} |")
    # End Loop
end_time = time.time()

log_display(f"[END] >> Simulation loop ends in {end_time - start_time:.4f}")
log(f"Simulation efficiency >> Real time per simulated second = {(end_time - start_time) / total_sim_time:.4f}")
log(f"Simulation efficiency >> Real time per simulated frame = {(end_time - start_time) / (total_sim_time * sim_resolution) :.4f}") 

log("Logging concludes. Running final changes to save log file")
try:
    os.rename(filename , savename)
except:
    log_display("[Error]: Failed to rename log file.")
    
    