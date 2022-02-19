#%% 
import pandas as pd
import os
os.chdir("C:/Users/kohssy/OneDrive - ooharastudent/Enhanced Python/pandas")
df = pd.read_csv('lunch_box.csv', sep=',')
# %%
# datetime列をindexにする
df.set_index('datetime', inplace=True)
# inplaceは変更するかの最終確認
df.head()

# %%
# カラム名を変更する（y を sales に変換）
df.rename(columns={'y': 'sales'}, inplace=True)
df.head()
# %%
# 'sales'列を降順で並び替えもできる
df.sort_values(by="sales", ascending=True).head() # ascending=Trueで昇順
# %%
# sort_valuesは複数の列に対しても実行できる
df.sort_values(['sales', 'temperature'], ascending=False).head() # ascending=Falseで昇順
# %%
# indexであるdatetimeのdtype='object' を dtype='datetime64[ns]' に変更
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
# indexがdatetime型のときにできること
# indexに対してsortを行う
df.sort_index().head() # object型のままだと正しくsortされない
# %%
# resampleメソッドで、日単位や月単位で簡単に集計できる
df.resample('M').mean() #月単位で平均値を出力
# %%
