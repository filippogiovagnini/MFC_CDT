import numpy as np
import matplotlib.pyplot as plt

u = 1.0
nx = 80
x = np.linspace(0.0, 1.0, nx + 1)
nt = 40
dx = 2./nx
dt = 1./nt

# \mu = u \frac{\Delta t}{\Delta x}
# If \mu > 1, the solution is unstable. If \mu < 1, the solution is stable.

# The spacial resolution
# The time step
# The initial conditions and arrays for the old and new time steps
phi = np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0.)
phiOld = phi.copy()
# Plot the initial conditions
plt.plot(x, phi, 'k', label = 'initial_conditions')
plt.legend(loc = 'best')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle = ':', color = 'black')
plt.ylim([0,1])

plt. pause(1)
# Loop over all time steps
for n in range(nt):
  for j in range(1,nx): # loop over space from 1 to nx-1
# (avoiding boundary conditions)
    phi[j] = phiOld[j] - u*dt*(phiOld[j] - phiOld[j - 1])/dx
  phiOld = phi.copy()
  plt.cla()
  plt.plot(x, phi, 'b', label = 'Time_' + str(n*dt))
  plt.legend(loc = 'best')
  plt.ylabel('$\phi$')
  plt.ylim([0,1])
  plt.pause(0.05)

plt.show()
