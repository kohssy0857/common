import numpy as np
# インポート

x = np.array([3, 4])
print(np.linalg.norm(x))
y = np.array([33, 56])
print(np.linalg.norm(y))
# ノルム（平方根の和）

a = np.array([[1], [2], [3]])
print(a)
print(a.T)
c = np.array([[1, 2], [3, 4]])
print(c)
print(c.T)
# 転置


a = np.array([[1, 2], [3, 4]])
print(a.trace())
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.trace())
# トレース(正方行列において１，１の対角和)



