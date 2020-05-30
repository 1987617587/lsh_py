# author : Lsh
# date: 2019/12/24 9:34
# file_name:tree3


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p)), rstride=1, cstride=1,
                       cmap=cm.gist_rainbow_r,
                       linewidth=0, antialiased=True)
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「lrd121」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/lrd121/article/details/76240450
