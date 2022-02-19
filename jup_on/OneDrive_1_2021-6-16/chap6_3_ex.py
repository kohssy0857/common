# numpy のインポート
import numpy as np
# my_deep_learning のインポート
import my_deep_learning as dl

# 乱数シードの設定
np.random.seed(1)

# 入力層の初期化 = 信号パターンの初期化
move_pattern = np.array( [
  [0, 1, 1, 0], # パターン１
  [1, 1, 1, 0], # パターン２
  [0, 1, 0, 1], # パターン３
  [1, 1, 0, 1]  # パターン４
] )
# 入力層のユニット数
input_layer_size = 

# 中間層のユニット数
hidden_layer_size = 

# 目的値リストの初期化 = 出力層の正解（教師信号）
direction = np.array([
  [1, 0, 0, 0], # パターン１（前進）
  [0, 1, 0, 0], # パターン２（左折）
  [0, 0, 1, 0], # パターン３（右折）
  [0, 0, 0, 1]  # パターン４（停止）
])
# 出力層のユニット数
output_layer_size = 

# 学習効率アルファの初期化
alpha = 0.2

# 重みの初期化
# 入力層と中間層間の重み
weight_i_h = 
# print('weight_i_h.shape = ', weight_i_h.shape)
# 中間層と出力層間の重み
weight_h_o = 
# print('weight_h_o.shape = ', weight_h_o.shape)

# 信号機の全パターンを１０回学習する
# 信号機全パターンを学習する

  print('信号パターン = {}'.format(pat_num+1))
  # パターンを取り出し、入力層に設定する
  input_layer = 

  # １０回学習する
  
    # 入力層のデータを元に予測し、結果を中間層に設定する
    hidden_layer = 
    # 中間層のデータを元に予測し、結果を出力層に設定する
    output_layer = 
    # 出力層の表示
    print('出力層 = ', output_layer)
    # 出力層の学習
    weight_i_h, weight_h_o = dl.back_propagation(input_layer, hidden_layer, output_layer, direction, weight_i_h, weight_h_o, alpha, pat_num)