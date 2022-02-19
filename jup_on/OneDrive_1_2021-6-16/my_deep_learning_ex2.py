# numpy インポート　別名 np
import numpy as np

# x が正なら x を、x が負なら 0 を返す関数 relu の定義
def relu(x):
  return (x > 0) * x

# output が正なら 1 を、負なら 0 を返す関数 relu2derive 関数の定義
def relu2deriv(output):
  return output > 0 # returns 1 for input > 0
                    # return 0 otherwise

# 予測を行う関数 neural_network(input, weight) の定義
'''
関数名：neural_network
引数：input = 入力データセットリスト、weight = 重み行列
処理：input と weight の加重和を計算する
戻り値：加重和リスト
'''


# 乱数発生により重み行列を生成する関数 create_weight(layer_1_num, layer_2_num) の定義
'''
関数名：create_weight
引数：layer_1_num = 層１の長さ、layer_2_num = 層２の長さ
処理：乱数を発生させて、layer_1_num 行、layer_2_num 列の行列に重みを設定する
戻り値：重み行列
'''



# 誤差逆伝播法による学習関数 
# back_propagation(input, hidden, output, goal, weight_i_h, weight_h_o) の定義
'''
関数名：back_propagation
引数：
  input = 入力層のデータセットリスト
  hidden = 中間層の予測値リスト
  output = 出力層の予測値リスト
  goal = 目的値行列
  weight_i_h = 入力層と中間層間の重み行列
  weight_h_o = 中間層と出力層間の重み行列
  input_num = 入力層に与えられるパターン番号
処理：誤差逆伝播法により学習する
戻り値：
  更新した入力層と中間層の重み行列と、更新した中間層と出力層間の重み行列
'''

