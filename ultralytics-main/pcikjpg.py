import os
import shutil
import random
from tqdm import tqdm  # 用于显示进度条


def random_select_images(source_dir, target_dir, num=500, extensions=('.jpg', '.jpeg')):
    """
    随机选择并复制图片到目标目录
    :param source_dir: 源目录路径
    :param target_dir: 目标目录路径
    :param num: 需要选择的图片数量
    :param extensions: 支持的图片扩展名（不区分大小写）
    """
    try:
        # 验证源目录是否存在
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"源目录 {source_dir} 不存在")

        # 获取所有符合条件的图片文件
        all_files = []
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(extensions):
                    all_files.append(os.path.join(root, file))

        # 验证文件数量是否足够
        if len(all_files) < num:
            raise ValueError(f"源目录只有 {len(all_files)} 张图片，不足要求的 {num} 张")

        # 随机选择文件
        selected = random.sample(all_files, num)

        # 创建目标目录
        os.makedirs(target_dir, exist_ok=True)

        # 复制文件并显示进度
        print(f"正在复制 {num} 张图片到 {target_dir}:")
        for src_path in tqdm(selected, unit='file'):
            dst_path = os.path.join(target_dir, os.path.basename(src_path))

            # 处理文件名冲突
            counter = 1
            while os.path.exists(dst_path):
                name, ext = os.path.splitext(os.path.basename(src_path))
                dst_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
                counter += 1

            shutil.copy2(src_path, dst_path)  # 保留文件元数据

        print(f"\n操作完成！已成功复制 {len(selected)} 张图片")

    except Exception as e:
        print(f"\n发生错误：{str(e)}")


if __name__ == "__main__":
    # 配置参数（按需修改）
    SOURCE_DIR = "D:/daima/ultralytics-main/ultralytics/datasets/new/images/train"  # 原始图片目录
    TARGET_DIR = "D:/daima/ultralytics-main/ultralytics/datasets/new/images/val"  # 目标目录
    SELECT_NUM = 500  # 需要选择的图片数量

    # 安装进度条库（如果尚未安装）
    try:
        from tqdm import tqdm
    except ImportError:
        print("正在安装进度条依赖...")
        import subprocess

        subprocess.check_call(["pip", "install", "tqdm"])
        from tqdm import tqdm

    # 执行选择操作
    random_select_images(SOURCE_DIR, TARGET_DIR, SELECT_NUM)