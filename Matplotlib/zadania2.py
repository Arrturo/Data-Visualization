import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data

# #1

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# z = np.linspace(0, 2 * np.pi)
# x = np.sin(z)
# y = 2 * np.cos(z)

# ax.plot(x, y, z)
# plt.show()

#2
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5), ('c', 'v', -20, -4), ('g', 'X', -45, -8), ('y', '_', -15, -4)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.legend()
plt.show()


# #3
# fig = plt.figure(figsize=plt.figaspect(0.5))
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# cmap = ['hsv', 'Pastel1', 'gist_earth', 'hot', 'GnBu']


# for i in cmap:
#     ax = fig.add_subplot(1, 5, cmap.index(i) + 1, projection='3d')
#     surf = ax.plot_surface(X, Y, Z, cmap=i, linewidth=1,antialiased=False)
#     ax.set_zlim(-1.01, 1.01)
#     # fig.colorbar(surf, shrink=0.5, aspect=10)
# plt.show()

# #4
# fig = plt.figure(figsize=(8, 3))


# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# color = ['r', 'g', 'y', 'm', 'c']
# o = 5
# for i in color:
#     o += 1
#     ax1 = fig.add_subplot(2, 5, color.index(i) + 1, projection='3d')
#     ax2 = fig.add_subplot(2, 5, o, projection='3d')
#     ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color=i)
#     ax2.bar3d(x, y, bottom, width, depth, top, shade=False, color=i)
#     # ax2.set_title('Wykres nie zacieniony')
# plt.show()

#5

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf2 = ax2.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0.1, antialiased=True)

# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# ax2.set_zlim(-1.01, 1.01)
# ax2.zaxis.set_major_locator(LinearLocator(10))
# ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))


# fig.colorbar(surf, shrink=0.5, aspect=5)
# fig.colorbar(surf2, shrink=0.5, aspect=5)
plt.show()
