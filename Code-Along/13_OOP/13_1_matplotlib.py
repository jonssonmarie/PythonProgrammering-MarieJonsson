"""
Matplotlib

     - matlab style
     - oop approach
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5,5)
f = np.sín(x)

print(x)

# matlab style interface
plt.figure(dpi = 100)
plt.plot(x,f)
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("y")
# plt.show() # needed for .py-script

# OOP approach

# instantiates the objects fig and ax from Figure and AxesSubplot 
fig, ax = plt.figure(dpi=100),plt.axes()
ax.plot(x, f) # the ax object has a plot
# calling the method set from ax object to set the axis, labels and title
ax.set(xlim = (-6,6), ylim = (-1.5,1.5), xlabel="x", ylabel="y", title="$\sin{x}$");
# plt.show() # needed for .py-script



# Subplots

# MATLAB-style

plt.figure(figsize=(16,5), dpi=100)
plt.subplot(1,2,1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title("Plots")
plt.legend(("sin(x)", "cos(x)"))

plt.subplot(1,2,2)
plt.plot(x, np.cos(x))
plt.title("cos(x)");
# plt.show() # needed for .py-script

# OOP approach

fig, ax = plt.subplots(1, 2, dpi=150, figsize=(10, 4))

rng = np.random.RandomState(42)
# randn - draws random number from normal distribution
data_normal_dist = rng.randn(1000)

ax[0].hist(data_normal_dist, bins=30, alpha=.5)
ax[0].set(title="Histogram", xlabel="x", ylabel="y")

size = 1000*rng.rand(100)
sc = ax[1].scatter(x=rng.randn(100), y=rng.randn(100), c= rng.randn(100), alpha=.3, cmap="viridis", s=size)
fig.colorbar(sc)
ax[1].set(title="Bubble chart", xlabel="x", ylabel="y")

plt.savefig("../assets/beautiful_plots.png", transparent=True, facecolor="white")
# plt.show() # needed for .py-script