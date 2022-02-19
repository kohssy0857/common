import numpy as np
# インポート

'''
属性	説明
T	いわゆる転置を返す。ndim(後述)<2のときは元の配列が返される。
data	配列のデータがどこから始まっているのかを示すPythonのバッファーオブジェクト。
dtype	ndarrayに含まれる要素が持つデータ型。
flags	メモリ上におけるndarrayのデータの格納の仕方(Memory Layout)についての情報。
flat	ndarrayを１次元配列に変換するイテレーター。
imag	ndarrayにおける虚数部分(imaginary part)。
real	ndarrayにおける実数部分(real part)。
size	ndarrayに含まれる要素の数。
itemsize	バイト単位での一つ一つの要素の大きさ。
nbytes	そのndarrayの要素によって占められるバイト単位でのメモリ総量。
ndim	ndarrayに含まれる次元の数。
shape	ndarrayの形状(shape)をタプルで表したもの。
strides	各次元方向に１つ隣の要素に移動するために必要なバイト数をタプルで表示したもの。
ctypes	ctypesモジュールで扱うためのイテレーター。
base	ndarrayのベースとなるオブジェクト(どのメモリを参照しているのか)。
'''
a = np.array([1, 2, 3])
b = np.array([2, 2, 0])
print(a.flags)
# メモリレイアウト情報表示
print(a.flat[2])
# aを１次元配列にしたときのn番目の要素を表示

c = np.array([1.-2.6j, 2.1+3.J, 4.-3.2j])
print(c)
# 複素数を要素とするndarrayインスタンスを生成

print(c.real)
# 実部
print(c.imag)
# 虚部

print(a.size)
print(b.size)
# 要素の数
print(a.itemsize)
print(b.itemsize)
# バイトオーダーでの要素１つ１つの長さ
print(a.nbytes)
print(b.nbytes)
# バイトオーダーでの配列の長さ
print(a.size * a.itemsize == a.nbytes)

print(a.ndim)
print(b.ndim)
# 次元数