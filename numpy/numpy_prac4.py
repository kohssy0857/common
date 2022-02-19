import numpy as np
# インポート

a = np.array([33, 44, 54, 23, 25, 55, 32, 76]) # 適当な配列を１つ作る。

print(np.average(a))# まずはaの平均を求めてみる。
a = a.reshape(2,4) # aのshapeを変更。
print(a)
print(np.average(a,axis=1))
# 軸指定

a = np.random.randint(100, size = (2, 3, 4))
print(a)
print(np.median(a))
# 中央値を指定
print(np.median(a,axis=1))
print(np.median(a,axis=2))
# averageに続き軸指定可

print(np.var(a))
# 分散（平均からの各要素の絶対値の二乗の合計）
print(np.var(a,ddof=1))
# 分散（(平均からの各要素の絶対値の二乗の合計)＊要素/(要素－1)）

print(np.std(a))
# 標準偏差（分散の平方根）
print(np.std(a,ddof=1))
# 不偏標準偏差 (不偏分散の平方根）
print(np.std(a, axis=(0, 1)))
# 2つ指定するとこの２つの軸方向に広がる平面内における標準偏差を求めてくれる



x = np.array([[1, 2, 1, 9, 10, 3, 2, 6, 7],[2, 1, 8, 3, 7, 5, 10, 7, 2]]) 
# 1行目が数学、2行目が国語の成績。
print(np.corrcoef(x))
# 相関関数行列を求める
'''
rの範囲	相関の度合い
-1 ≤ r < -0.7	強い負の相関
-0.7 ≤ r < -0.4	負の相関
-0.4 ≤ r < -0.2	弱い負の相関
-0.2 ≤ r < 0.2	相関がほとんどない
0.2 ≤ r < 0.4	弱い正の相関
0.4 ≤ r < 0.7	正の相関
0.7 ≤ r ≤ 1	強い正の相関
'''
y = np.array([2, 1, 1, 8, 9, 4, 3, 5, 7]) 
# 英語の成績を追加。
print(np.corrcoef(x, y))
'''
 	      数学	      国語	     英語
数学	数学-数学	数学-国語	数学-英語
国語	国語-数学	国語-国語	国語-英語
英語	英語-数学	英語-国語	英語-英語
'''