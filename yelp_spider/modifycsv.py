import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'E:\Internship\crawler_practice-master\yelp_spider\restaurants.csv')

# 修改Price Range列的值
df['Price Range'] = df['Price Range'].replace({'$': 'below $10', '$$': '$11-30', '$$$': '$31-60', '$$$$': 'over $61'})
print(df['Features'])

# 修改Features列的值
df['Features'] = df['Features'].str.replace('×', 'not allow')
df['Features'] = df['Features'].str.replace('√', 'allow')
df['Features'] = df['Features'].str.replace('[', '')
df['Features'] = df['Features'].str.replace(']', '')
df['Features'] = df['Features'].str.replace('\'', '')

# 保存修改后的数据到新的CSV文件
df.to_csv('modified_restaurants.csv', index=False)
print("File 'modified_restaurants.csv' saved successfully.")
