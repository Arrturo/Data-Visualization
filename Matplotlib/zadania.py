from math import *
import numpy as np
import matplotlib.pyplot as plt
# #1
# y = [1/y for y in range(1, 21)]
# plt.plot(y, label='f(x)=1/x')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x)= 1/x w przedziale [1,20]')
# plt.show()

# #2
# y = [1/y for y in range(1, 21)]
# plt.axis([0, 20, 0, 1])
# plt.plot(y, 'g^--', label='f(x)=1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x)= 1/x w przedziale [1,20]')
# plt.show()

# #3
x = np.arange(0, 30, 0.1)
sin = np.sin(x)
cos = np.cos(x)

plt.plot(sin, 'b', label='sin(x)')
plt.plot(cos, 'r', label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')
plt.title('Wykres sin(x) i cos(x) w przedziale [0,30]')
plt.show()

# #4
# x = np.arange(0, 30, 0.1)
# b = np.sin(x)
# c = np.sin(-x)-2
# plt.plot(x, b, 'b', label='sin(x)')
# plt.plot(x, c, 'r', label='sin(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title("Wykres sin(x), sin(x)")
# plt.show()



