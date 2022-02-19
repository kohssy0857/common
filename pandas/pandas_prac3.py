#%% 
import pandas as pd
import os
os.chdir("C:/Users/kohssy/OneDrive - ooharastudent/Enhanced Python/pandas")
df = pd.read_csv('lunch_box.csv', sep=',')
# %%
# 列単位で 欠損値NaN(not a number)が入っている個数をカウントする （正確には、isnull()でtrueが返ってくる個数をカウントしている）
df.isnull().sum()
# %%
# 1つでもNaNが含まれる行だけを抽出（最初の5行のみ表示）
print(df[df.isnull().any(axis=1)].shape)
df[df.isnull().any(axis=1)].head()
# %%
# 'payday'列にあるNaNを'0.0'に置き換える
df.fillna(value={'payday': 0.0}, inplace=True)
df.head()
# %%
# 'kcal'列にNaNがある行を削除する
df.dropna(subset=['kcal'], axis=0, inplace=True)
print(df.shape) # 207-166=41行のデータを削除した
# %%
# 'precipitation' 列の '--' を 0に置き換える
df['precipitation'] = df['precipitation'].str.replace('--', 0).astype(float)
df.head()
# %%
# maskメソッドを使う例。'y'列が80よりも大きければ、その値を100に置換する
pd.DataFrame(df['y'].mask(df['y'] > 80, 100)).head()
# %%
# weather列の集計
df['weather'].value_counts()
# %%
# groupbyメソッドで、'week'列ごとに'soldout'の数をカウントする
df.groupby(['week'])['soldout'].count()
# %%
