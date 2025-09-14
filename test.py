import os

def check_path_exists(path):
    # 检查路径是否存在
    if os.path.exists(path):
        print(f"路径 '{path}' 存在。")
    else:
        print(f"路径 '{path}' 不存在。")

# 获取当前工作目录
current_directory = os.getcwd()

# 打印当前工作目录
print("当前路径是:", current_directory)

# 使用示例
path_to_check = input("请输入要检查的路径：")
while path_to_check != 'q':
    check_path_exists(path_to_check)
    path_to_check = input("请输入要检查的路径：")
