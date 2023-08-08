import os
import pandas as pd

# 设置文件夹路径
folder_paths = ['Bronx', 'Brooklyn', 'Manhatten', 'Queens', 'Staten Island']

# 创建一个空的DataFrame用于存储合并后的数据
merged_df = pd.DataFrame()

# 循环遍历每个文件夹路径
for folder_path in folder_paths:
    file_path = os.path.join(folder_path, 'modified_restaurants.csv')

    # 读取CSV文件为DataFrame
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        # 将当前文件夹的数据合并到总的DataFrame中
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# 保存合并后的数据到新文件
merged_file_path = 'merged_reataurants.csv'
merged_df.to_csv(merged_file_path, index=False)

print("合并完成并已保存到", merged_file_path)
