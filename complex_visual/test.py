from main import ComplexVisual
import numpy as np


#testing paramplot 1#
phi = lambda t: [t*np.cos(t),(t**2)*np.sin(t)]
f = lambda z: 1/z
ComplexVisual.curve_plot(f,phi,a=-10,b=10)

# a = -10
# b = 10

# phi = lambda t: [-1/2*(t/t),t-t]
# f = lambda z: 1/z
# ComplexVisual.curve_plot(f,phi,a=1,b=10)





