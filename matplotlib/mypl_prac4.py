import math
import numpy as np
from matplotlib import pyplot as plt

x = [10, 51, 44, 23, 55, 95]
y = [5, 125, 2, 55, 19, 55]
plt.scatter(x,y)
# 散布図
plt.show()


# 平均10、標準偏差10 の正規乱数を100件生成
x = np.random.normal(10, 10, 1000)

plt.hist(x)
# ヒストグラムを表示
plt.show()
# 引数にbins=数字でヒストグラムの棒の数を指定できます。
# plt.hist(x, bins=16)