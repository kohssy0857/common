import math
import numpy as np
from matplotlib import pyplot as plt

pi = math.pi   #mathモジュールのπを利用

x = np.linspace(0, 2*pi, 100)  #0から2πまでの範囲を100分割したnumpy配列
y = np.sin(x)

plt.plot(x, y)
plt.show()

#凡例のためにlabelキーワードで凡例名をつける
plt.plot(x, y, label='sin')

#グラフタイトル
plt.title('Sin Graph')

#グラフの軸
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#グラフの凡例
plt.legend()

plt.show()