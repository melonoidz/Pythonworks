# -*- coding: UTF-8 -*-
# 受け取ったcsvをarray入力する
# 3D表示する
import glob
import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 表示領域の設定
box_size = 10.0
# csvの入力
csv_files = sorted(glob.glob('*.csv'))


# 縮小倍率
limit = 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for i in range(len(csv_files)/3-1):
        # CSV入力
        x = np.loadtxt('xframe' + str(i+1) + '.csv', delimiter=',')
        y = np.loadtxt('yframe' + str(i+1) + '.csv', delimiter=',')
        z = np.loadtxt('zframe' + str(i+1) + '.csv', delimiter=',')
        xnp = x / limit
        ynp = y / limit
        znp = z / limit

        ax.set_autoscalez_on(False)
        # view_init(縦, 横) ≦90がよい
        ax.view_init(45, 90)
        plt.cla()
        ax.scatter(xnp, ynp, znp)

        # 骨格点
        p0 = (xnp[0], ynp[0], znp[0])
        p1 = (xnp[1], ynp[1], znp[1])
        p2 = (xnp[2], ynp[2], znp[2])
        p3 = (xnp[3], ynp[3], znp[3])
        p4 = (xnp[4], ynp[4], znp[4])
        p5 = (xnp[5], ynp[5], znp[5])
        p6 = (xnp[6], ynp[6], znp[6])
        p7 = (xnp[7], ynp[7], znp[7])
        p8 = (xnp[8], ynp[8], znp[8])
        p9 = (xnp[9], ynp[9], znp[9])
        p10 = (xnp[10], ynp[10], znp[10])
        p11 = (xnp[11], ynp[11], znp[11])
        p12 = (xnp[12], ynp[12], znp[12])
        p13 = (xnp[13], ynp[13], znp[13])

        ax.plot(*zip(p1, p0))
        ax.plot(*zip(p1, p2))
        ax.plot(*zip(p1, p5))
        ax.plot(*zip(p2, p3))
        ax.plot(*zip(p3, p4))
        ax.plot(*zip(p5, p6))
        ax.plot(*zip(p6, p7))
        ax.plot(*zip(p1, p8))
        ax.plot(*zip(p1, p11))
        ax.plot(*zip(p8, p9))
        ax.plot(*zip(p9, p10))
        ax.plot(*zip(p11, p12))
        ax.plot(*zip(p12, p13))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        filename = str(i+1) + ".png"
        plt.savefig(filename)
