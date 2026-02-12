import numpy as np 
import matplotlib.pyplot as plt

# 1. Parameters 
a1 = 0.25     
a2 = 0.05     
b1 = 1.5       
b2 = 0.15      
b3 = 0.35      
kpbr = 0.018  
c2 = 0.45     
V_max = 1000   
alpha = 300    

# 2. Simulation setup
sim_length = 200 
dt = 0.01 
time = np.arange(0, sim_length, dt)
steps = len(time)

# 3. Initialize arrays
V = np.zeros(steps)
R = np.zeros(steps)

# 4. Initial conditions
V[0] = 800
R[0] = 50

# 5. Simulation loop 
for i in range(steps - 1):
    V_curr = V[i]
    R_curr = R[i]
 #  Vegetation Dynamics
    Rv = a1 * (1 - V_curr/V_max) * V_curr  
    Mv = a2 * V_curr                     
    
    # Grazing Logic
    if V_curr >= alpha:
        Dv = b1 * R_curr                 
    else:
        # Mode 2 and 3
        Dv = V_curr * c2 
    
    dVdt = Rv - Mv - Dv
    
    # Reindeer Dynamics
    # Population Growth Logic
    if V_curr >= alpha:
        Rr = Dv * kpbr                   
    else:
        Rr = 0                           
    
    # Mortality Logic 
    if V_curr >= (alpha * 0.8):
        Mr = R_curr * b2                 
    else:
        Mr = R_curr * b3                  
    
    dRdt = Rr - Mr
    
    # Euler Integration
    V[i+1] = V_curr + dVdt * dt
    R[i+1] = R_curr + dRdt * dt


# 6. Plotting
plt.figure(figsize=(10, 5))
plt.plot(time, V, label='Lichens (tons/100km$^2$)', color='green')
plt.plot(time, R, label='Reindeer population', color='brown')
plt.axhline(y=alpha, color='r', linestyle='--', label='Critical Level ($\\alpha$)')
plt.xlabel('Time (years)')
plt.ylabel('Amount')
plt.title('Vegetation-Reindeer Dynamics')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
