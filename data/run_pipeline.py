import pandas as pd

# 1. 读取分页爬虫生成的 CSV
books_df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\books_pagination.csv"
)

# 2. 打印数据规模
print("原始数据规模：", books_df.shape)

# 3. 检查缺失值
print("缺失值统计：")
print(books_df.isna().sum())

# 4. 检查重复标题
duplicate_books = books_df[
    books_df.duplicated(
        subset=["title"],
        keep=False
    )
]

print("重复书籍数量：", len(duplicate_books))

# 5. 生成最终清洗文件
output_path = (
    r"D:\Codex项目\数据岗位冲刺\data"
    r"\books_pipeline_result.csv"
)

books_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("最终文件已保存：", output_path)