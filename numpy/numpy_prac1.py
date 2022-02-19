import numpy as np
# インポート
a = np.array([1, 2, 3])
print(a)
# numpy配列の作成
a*=3
print(a)
# 配列自体と整数の積
a+=4
print(a)
# 配列自体と整数の和

b = np.array([2, 2, 0])

print(a+b)
# 配列の各要素ごとの和
print(a*b)
# 配列の各要素ごとの積（アダマール積）
print(a/b)
# 配列の各要素ごとの商（0で割っているのでINF）
print(np.dot(a,b))
# 各要素ごとの積の和（内積）

ran=np.arange(10)
print(ran)
# 終点のみのrange
ran2=np.arange(0,10,2)
print(ran2)
# np.arange(始点,終点,ステップ) 終点は配列に含まれない
lins=np.linspace(0,10,15)
print(lins)
# 始点から終点（終点含む）をステップ数で分割する

c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
# 二次元配列
print(c.shape)
# 配列の形状を表示

d=np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]])
print(d)
# 三次元配列
print(d.shape)
# 配列の形状を表示

print(np.sum(c))
# すべての積
print(np.sum(c, axis=0))
print(np.sum(c, axis=1))
# axis(軸)を設定することで外からn-1番目にネストされた要素で演算される

print(c.reshape(3,2))
print(c.reshape(1,6))
# 配列の形状を変更
# 配列の要素数の合計＝＝引数の積

randn=np.random.randn()
print(randn)
# 正規分布に従う0~1までの乱数
rand=np.random.rand()
print(rand)
#0~1までの乱数
randArr=np.random.randn(2,3)
print(randArr)
# 3つの乱数が入った配列を二つ作る

e = np.array([0, 5, 2, 7, 1, 9])

print(e[::-1])
# スライスを使った逆順ソート