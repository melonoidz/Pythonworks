# -*- coding: UTF-8 -*-
# vector差分を計算する
# 平面方向は肩L25、垂直方向はL01を基準にする？
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
# 縮尺
limit = 1
# list
xroundlist = []
yroundlist = []
sroundlist = []

lxplist = []
lyplist = []
xrlist = []
# 最初の1フレームの読み込み
x = np.loadtxt('xframe1.csv', delimiter=',')
y = np.loadtxt('yframe1.csv', delimiter=',')
z = np.loadtxt('zframe1.csv', delimiter=',')

# 肩幅vectorの定義
# 平面方向
a1 = x[3] - x[6]
b = y[3] - y[6]
c = z[3] - z[6]
lx = np.array([a1, b, c])

# 垂直方向
d = x[1] - x[0]
e = y[1] - y[0]
f = z[1] = z[0]
ly = np.array([d, e, f])

g = x[3]
h = x[6]
i = y[3]
j = y[6]


# 180度以上も表示するようにする
def angle(x, y):

    dot_xy = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos = dot_xy / (norm_x*norm_y)
    rad = np.arccos(cos)
    theta = rad * 180 / np.pi
    return theta


# フレームごとのベクトル
for i in range(len(csv_files)/3-1):
        # CSV入力
        x = np.loadtxt('xframe' + str(i+1) + '.csv', delimiter=',')
        y = np.loadtxt('yframe' + str(i+1) + '.csv', delimiter=',')
        z = np.loadtxt('zframe' + str(i+1) + '.csv', delimiter=',')
        xnp = x / limit
        ynp = y / limit
        znp = z / limit

        # 平面方向
        a = x[3] - x[6]
        b = y[3] - y[6]
        c = z[3] - z[6]
        lxp = np.array([a, b, c])
        lxplist.append(lxp)
        # 垂直方向
        d = x[1] - x[0]
        e = y[1] - y[0]
        f = z[1] = z[0]
        lyp = np.array([d, e, f])
        lyplist.append(lyp)

# 180度以上の増分を出力できるようにする
# それぞれ角度を計算し足し合わせる
for j in range(len(csv_files)/3-1):
    xr = angle(lxplist[j-1], lxplist[j])
    xrlist.append(xr)

sum = 0
for k in range(len(xrlist)):
    sum += xrlist[k]
    print sum

print len(xrlist)
