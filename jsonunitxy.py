# -*- coding: UTF-8 -*-
# 時間差分をとって座標計算
# 連続するjsonを読み込みグラフ化し数値出力もする
# people内が空のjsonを省く
# 0に注意する
# x,yそれぞれをcsv出力する
import glob
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# json読み込み
json_fnames = sorted(glob.glob("*.json"))

q = np.zeros((1, 14))
r = np.zeros((1, 14))
# listに格納(0~13)
# 0
x0list = []
y0list = []
# 1
x1list = []
y1list = []
# 2
x2list = []
y2list = []
# 3
x3list = []
y3list = []
# 4
x4list = []
y4list = []
# 5
x5list = []
y5list = []
# 6
x6list = []
y6list = []
# 7
x7list = []
y7list = []
# 8
x8list = []
y8list = []
# 9
x9list = []
y9list = []
# 10
x10list = []
y10list = []
# 11
x11list = []
y11list = []
# 12
x12list = []
y12list = []
# 13
x13list = []
y13list = []

# 0代入
for i in json_fnames:
    with open(i, 'r') as f:
        data = json.load(f)
        if len(data[data.keys()[1]]) == 0:
            data[data.keys()[1]] = [{u'face_keypoints': [],
                                     u'pose_keypoints': [0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0, 0, 0, 0,
                                                         0, 0, 0, 0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0, 0, 0, 0,
                                                         0, 0, 0, 0,
                                                         0, 0, 0, 0, 0],
                                     u'hand_right_keypoints': [],
                                     u'hand_left_keypoints': []}]
    # xyz
    x0 = data[data.keys()[1]][0]["pose_keypoints"][0]
    y0 = data[data.keys()[1]][0]["pose_keypoints"][1]
    x1 = data[data.keys()[1]][0]["pose_keypoints"][3]
    y1 = data[data.keys()[1]][0]["pose_keypoints"][4]
    x2 = data[data.keys()[1]][0]["pose_keypoints"][6]
    y2 = data[data.keys()[1]][0]["pose_keypoints"][7]
    x3 = data[data.keys()[1]][0]["pose_keypoints"][9]
    y3 = data[data.keys()[1]][0]["pose_keypoints"][10]
    x4 = data[data.keys()[1]][0]["pose_keypoints"][12]
    y4 = data[data.keys()[1]][0]["pose_keypoints"][13]
    x5 = data[data.keys()[1]][0]["pose_keypoints"][15]
    y5 = data[data.keys()[1]][0]["pose_keypoints"][16]
    x6 = data[data.keys()[1]][0]["pose_keypoints"][18]
    y6 = data[data.keys()[1]][0]["pose_keypoints"][19]
    x7 = data[data.keys()[1]][0]["pose_keypoints"][21]
    y7 = data[data.keys()[1]][0]["pose_keypoints"][22]
    x8 = data[data.keys()[1]][0]["pose_keypoints"][24]
    y8 = data[data.keys()[1]][0]["pose_keypoints"][25]
    x9 = data[data.keys()[1]][0]["pose_keypoints"][27]
    y9 = data[data.keys()[1]][0]["pose_keypoints"][28]
    x10 = data[data.keys()[1]][0]["pose_keypoints"][30]
    y10 = data[data.keys()[1]][0]["pose_keypoints"][31]
    x11 = data[data.keys()[1]][0]["pose_keypoints"][33]
    y11 = data[data.keys()[1]][0]["pose_keypoints"][34]
    x12 = data[data.keys()[1]][0]["pose_keypoints"][36]
    y12 = data[data.keys()[1]][0]["pose_keypoints"][37]
    x13 = data[data.keys()[1]][0]["pose_keypoints"][39]
    y13 = data[data.keys()[1]][0]["pose_keypoints"][40]

    # listに格納
    x0list.append(x0)
    y0list.append(y0)
    x1list.append(x1)
    y1list.append(y1)
    x2list.append(x2)
    y2list.append(y2)
    x3list.append(x3)
    y3list.append(y3)
    x4list.append(x4)
    y4list.append(y4)
    x5list.append(x5)
    y5list.append(y5)
    x6list.append(x6)
    y6list.append(y6)
    x7list.append(x7)
    y7list.append(y7)
    x8list.append(x8)
    y8list.append(y8)
    x9list.append(x9)
    y9list.append(y9)
    x10list.append(x10)
    y10list.append(y10)
    x11list.append(x11)
    y11list.append(y11)
    x12list.append(x12)
    y12list.append(y12)
    x13list.append(x13)
    y13list.append(y13)

    # arrayに格納
    x0np = np.array(x0list)
    x1np = np.array(x1list)
    x2np = np.array(x2list)
    x3np = np.array(x3list)
    x4np = np.array(x4list)
    x5np = np.array(x5list)
    x6np = np.array(x6list)
    x7np = np.array(x7list)
    x8np = np.array(x8list)
    x9np = np.array(x9list)
    x10np = np.array(x10list)
    x11np = np.array(x11list)
    x12np = np.array(x12list)
    x13np = np.array(x13list)

    y0np = np.array(y0list)
    y1np = np.array(y1list)
    y2np = np.array(y2list)
    y3np = np.array(y3list)
    y4np = np.array(y4list)
    y5np = np.array(y5list)
    y6np = np.array(y6list)
    y7np = np.array(y7list)
    y8np = np.array(y8list)
    y9np = np.array(y9list)
    y10np = np.array(y10list)
    y11np = np.array(y11list)
    y12np = np.array(y12list)
    y13np = np.array(y13list)

    # スムージング処理
    for j in range(len(x0np)):
        if x0np[j] == 0:
            x0np[j] = x0np[j-1]
        if x1np[j] == 0:
            x1np[j] = x1np[j-1]
        if x2np[j] == 0:
            x2np[j] = x2np[j-1]
        if x3np[j] == 0:
            x3np[j] = x3np[j-1]
        if x4np[j] == 0:
            x4np[j] = x4np[j-1]
        if x5np[j] == 0:
            x5np[j] = x5np[j-1]
        if x6np[j] == 0:
            x6np[j] = x6np[j-1]
        if x7np[j] == 0:
            x7np[j] = x7np[j-1]
        if x8np[j] == 0:
            x8np[j] = x8np[j-1]
        if x9np[j] == 0:
            x9np[j] = x9np[j-1]
        if x10np[j] == 0:
            x10np[j] = x10np[j-1]
        if x11np[j] == 0:
            x11np[j] = x11np[j-1]
        if x12np[j] == 0:
            x12np[j] = x12np[j-1]
        if x13np[j] == 0:
            x13np[j] = x13np[j-1]

    for k in range(len(y0np)):
        if y0np[k] == 0:
            y0np[k] = y0np[k-1]
        if y1np[k] == 0:
            y1np[k] = y1np[k-1]
        if y2np[k] == 0:
            y2np[k] = y2np[k-1]
        if y3np[k] == 0:
            y3np[k] = y3np[k-1]
        if y4np[k] == 0:
            y4np[k] = y4np[k-1]
        if y5np[k] == 0:
            y5np[k] = y5np[k-1]
        if y6np[k] == 0:
            y6np[k] = y6np[k-1]
        if y7np[k] == 0:
            y7np[k] = y7np[k-1]
        if y8np[k] == 0:
            y8np[k] = y8np[k-1]
        if y9np[k] == 0:
            y9np[k] = y9np[k-1]
        if y10np[k] == 0:
            y10np[k] = y10np[k-1]
        if y11np[k] == 0:
            y11np[k] = y11np[k-1]
        if y12np[k] == 0:
            y12np[k] = y12np[k-1]
        if y13np[k] == 0:
            y13np[k] = y13np[k-1]

for l in range(len(x0np)):
    q[0, 0] = x0np[l]
    q[0, 1] = x1np[l]
    q[0, 2] = x2np[l]
    q[0, 3] = x3np[l]
    q[0, 4] = x4np[l]
    q[0, 5] = x5np[l]
    q[0, 6] = x6np[l]
    q[0, 7] = x7np[l]
    q[0, 8] = x8np[l]
    q[0, 9] = x9np[l]
    q[0, 10] = x10np[l]
    q[0, 11] = x11np[l]
    q[0, 12] = x12np[l]
    q[0, 13] = x13np[l]
    # 2次元arrayの保存
    # csvファイルとして保存
    np.savetxt('xframe' + str(l+1) + '.csv', q, delimiter=',')

for m in range(len(y0np)):
    r[0, 0] = y0np[m]
    r[0, 1] = x1np[m]
    r[0, 2] = x2np[m]
    r[0, 3] = x3np[m]
    r[0, 4] = x4np[m]
    r[0, 5] = x5np[m]
    r[0, 6] = x6np[m]
    r[0, 7] = x7np[m]
    r[0, 8] = x8np[m]
    r[0, 9] = x9np[m]
    r[0, 10] = x10np[m]
    r[0, 11] = x11np[m]
    r[0, 12] = x12np[m]
    r[0, 13] = x13np[m]
    # 2次元arrayの保存
    # csvファイルとして保存
    np.savetxt('yframe' + str(m+1) + '.csv', r, delimiter=',')
