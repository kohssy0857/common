import numpy as np
# インポート


a = np.arange(1,11)
print(a)
b = np.array([1,2,1,2,1,2,1,2,1,2])
print(b)

print(a**b)
# 基数＊＊指数

print(np.sin(a))#正弦
print(np.cos(a))#余弦
print(np.tan(a))#正接
# 逆三角関数はarcを接頭

print(np.e)
# ネイピア数

'''
切り捨てnp.floor()
切り捨てnp.trunc()
切り上げnp.ceil()
四捨五入np.round()
四捨五入np.around()
四捨五入np.rint()
0に近い方向で整数をとるnp.fix()
'''

print(np.absolute(a))
# 絶対値を返す（複素数を含む）
