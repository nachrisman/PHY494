import matplotlib.pyplot as plt

def heaviside(x):
    """Heaviside step function"""

    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = (1/2)
    else:
        theta = 1
    return theta

x = -4
xmax = 4
theta = []
xvalues = []

while x <= xmax:
    a = heaviside(x)
    xvalues.append(x)
    theta.append(a)
    x += 0.5

print(xvalues, theta)

plt.plot(xvalues, theta, '-o', color="red", linewidth=2)
plt.show()
