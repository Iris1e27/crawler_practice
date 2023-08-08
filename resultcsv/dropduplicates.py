import pandas as pd

# 读取原始CSV文件
file_path = 'merged_reataurants.csv'
df = pd.read_csv(file_path)

# 根据 "Detail URL" 列进行去重
deduplicated_df = df.drop_duplicates(subset='Detail URL')

# 保存去重后的数据到新文件
deduplicated_file_path = 'deduplicated_reataurants.csv'
deduplicated_df.to_csv(deduplicated_file_path, index=False)

print("去重完成并已保存到", deduplicated_file_path)
