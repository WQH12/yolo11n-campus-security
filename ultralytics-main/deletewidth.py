import os
import shutil

# 当前文件夹的绝对路径（填写您的当前文件夹路径）
current_folder = "D:/daima/ultralytics-main/ultralytics/datasets/new/labels/train"  # <-- 替换为您的当前文件夹路径

# 目标文件夹的绝对路径（填写您想将文件复制到的文件夹路径）
target_folder = "D:/daima/ultralytics-main/ultralytics/datasets/new/labels/val"  # <-- 替换为您的目标文件夹路径

# 如果目标文件夹不存在，则创建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 读取val.txt文件中的内容
val_file_path = os.path.join(current_folder, 'val.txt')
with open(val_file_path, 'r') as file:
    filenames = [line.rstrip('\n') for line in file]

# 遍历val文件中的文件名，并复制对应的txt文件
for filename in filenames:
    # 将文件后缀从.jpg改为.txt
    txt_filename = filename.replace('.jpg', '.txt')
    # 构建源文件的完整路径
    source_file = os.path.join(current_folder, txt_filename)
    target_file = os.path.join(target_folder, txt_filename)

    # 检查文件是否存在
    if os.path.exists(source_file):
        shutil.copy(source_file, target_file)
        print(f"已复制: {txt_filename}")
    else:
        print(f"未找到: {txt_filename}")

print(f"操作完成，共处理了 {len(filenames)} 个文件")