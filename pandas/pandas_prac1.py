#%% 
import pandas as pd
import os
os.chdir("C:/Users/kohssy/OneDrive - ooharastudent/Enhanced Python/pandas")
df = pd.read_csv('lunch_box.csv', sep=',')
# 読み込み（,でのCSV読み込み）
df.head(3)
# データの確認をする（最初の3行を表示）
# %%
# 先頭の5行を表示
df.head()
# %%
# 最後尾の5行を表示
df.tail()
# %%
print('dataframeの行数・列数の確認==>\n', df.shape)
print('indexの確認==>\n', df.index)
print('columnの確認==>\n', df.columns)
print('dataframeの各列のデータ型を確認==>\n', df.dtypes)
# %%
# 任意の列だけ取り出したい場合
df[['name', 'kcal']].head()
# %%
# 100行目から105行目まで表示したい場合
df[100:106]
# %%
# indexが100の行だけ取得したい場合
df.loc[100]

# %%
# もっとピンポイントに抽出したい場合
# 例: 1,2,4 行目と 0-2 列目を取得
df.iloc[[1,2,4],[0,2]]
# %%
# 条件を指定して抽出
df[df['kcal'] > 450]
# %%
# queryメソッドを使うと、複数条件の指定で、特定カラムだけ出力もできる
df[['name', 'kcal']].query('kcal > 450 and name == "豚肉の生姜焼"') #query内のシングル/ダブルクオーテーションの使い方に注意
# %%
# 'remarks(備考)'には例えばどんなデータが入っているか確認
df['remarks'].unique()
# %%
# datatime単位で重複したデータが存在しないか確認
# ユニークな行数と全行の照らし合わせ
print(len(df) == len(df['datetime'].unique()))
# %%
#行方向で重複行を削除
df.drop_duplicates() 
# %%
