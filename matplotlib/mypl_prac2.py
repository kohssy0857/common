import math
import numpy as np
from matplotlib import pyplot as plt

pi = math.pi

x = np.linspace(0, 2*pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)  #新たにcosを計算

plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')  #cosの値をプロット

#グラフタイトル
plt.title('Sin And Cos Graph')

#グラフの軸
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#グラフの凡例
plt.legend()

plt.show()