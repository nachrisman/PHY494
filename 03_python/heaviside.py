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
x = 3
theta = heaviside(x)

print("Theta(" + str(x) + ") = " + str(theta))
