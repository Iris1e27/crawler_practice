import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'merged_restaurants.csv')

# 修改Price Range列的值
df['Price Range'] = df['Price Range'].replace({'$': 'below $10', '$$': '$11-30', '$$$': '$31-60', '$$$$': 'over $61'})
print(df['Features'])

# 修改Features列的值
df['Features'] = df['Features'].str.replace('×', 'not allow')
df['Features'] = df['Features'].str.replace('√', 'allow')
df['Features'] = df['Features'].str.replace('[', '')
df['Features'] = df['Features'].str.replace(']', '')
df['Features'] = df['Features'].str.replace('\'', '')

# Opening Hours
df['Opening Hours'] = df['Opening Hours'].str.replace('[', '')
df['Opening Hours'] = df['Opening Hours'].str.replace(']', '')
df['Opening Hours'] = df['Opening Hours'].str.replace('\'', '')

# Popular Dishes
df['Popular Dishes'] = df['Popular Dishes'].str.replace('[', '')
df['Popular Dishes'] = df['Popular Dishes'].str.replace(']', '')
df['Popular Dishes'] = df['Popular Dishes'].str.replace('\'', '')

# Detailed Address
# insert_position = df['Detailed Address'].str.len() - 10 - len(NY_AREA)
# df['Detailed Address'] = df.apply(lambda row: row['Detailed Address'][:insert_position[row.name]] + ", " + row['Detailed Address'][insert_position[row.name]:], axis=1)

# 保存修改后的数据到新的CSV文件
df.to_csv('modified_restaurants.csv', index=False)
print("File 'modified_restaurants.csv' saved successfully.")
