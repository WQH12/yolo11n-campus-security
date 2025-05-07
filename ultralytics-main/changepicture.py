import os
from PIL import Image
from pathlib import Path


def convert_png_to_jpg(input_dir, output_dir, quality=75):
    """
    将指定目录中的所有PNG图片转换为JPG格式
    :param input_dir: 输入目录路径
    :param output_dir: 输出目录路径
    :param quality: JPG质量 (1-100)
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    converted = 0
    errors = []

    # 遍历输入目录
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)

            try:
                # 打开图片文件
                with Image.open(input_path) as img:
                    # 移除Alpha通道（如果存在）
                    if img.mode in ('RGBA', 'LA'):
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[-1])
                        img = background

                    # 生成输出路径
                    output_filename = os.path.splitext(filename)[0] + '.jpg'
                    output_path = os.path.join(output_dir, output_filename)

                    # 保存为JPG
                    img.convert('RGB').save(output_path, 'JPEG', quality=quality)
                    converted += 1

            except Exception as e:
                errors.append(f"{filename}: {str(e)}")

    # 输出报告
    print(f"转换完成！成功转换 {converted} 张图片")
    if errors:
        print("\n遇到以下错误：")
        for error in errors:
            print(f"  - {error}")


if __name__ == "__main__":
    # 配置参数（按需修改）
    INPUT_DIR = "D:/dataset/VOCdevkit 4/VOC2007/JPEGImages"  # 原始PNG文件目录
    OUTPUT_DIR = "D:/dataset/VOCdevkit 4/VOC2007/jpg_images"  # 输出JPG目录
    QUALITY = 85  # 图片质量 (1-100)

    # 执行转换
    convert_png_to_jpg(INPUT_DIR, OUTPUT_DIR, QUALITY)