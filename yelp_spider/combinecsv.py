import pandas as pd

# 读取1.csv和2.csv文件
df1 = pd.read_csv('restaurants.csv')
df2 = pd.read_csv('subpage.csv')

# 合并数据框，将df2的列添加到df1的后面
merged_df = pd.concat([df1, df2], axis=1)

# 将合并后的数据框保存为新的CSV文件（可选）
merged_df.to_csv('merged_restaurants.csv', index=False)

# 打印合并后的数据框（可选）
print(merged_df)
