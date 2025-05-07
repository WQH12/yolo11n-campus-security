import os
import xml.etree.ElementTree as ET


def xml_to_yolo(xml_file, class_dict, output_dir):
    """ 转换单个XML文件并保存到指定目录 """
    # 解析XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 获取图像尺寸
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # 生成YOLO格式内容
    yolo_lines = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        class_id = class_dict.get(cls, -1)  # 处理未知类别

        if class_id == -1:
            print(f"警告：发现未定义类别 '{cls}'，已跳过")
            continue

        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # 计算归一化坐标
        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

    # 写入文件
    if yolo_lines:
        output_path = os.path.join(output_dir, os.path.basename(xml_file).replace('.xml', '.txt'))
        with open(output_path, 'w') as f:
            f.write('\n'.join(yolo_lines))
        return True
    return False


def batch_convert(xml_dir, class_dict, output_dir):
    """ 批量转换整个目录 """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 遍历所有XML文件
    converted = 0
    for filename in os.listdir(xml_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(xml_dir, filename)
            if xml_to_yolo(xml_path, class_dict, output_dir):
                converted += 1
    print(f"转换完成！共处理 {converted} 个文件")


# 使用示例
class_dict = {
    'pothole': 4,
}

batch_convert(
    xml_dir="D:/dataset/VOCdevkit 4/VOC2007/Annotations",
    class_dict=class_dict,
    output_dir="D:/dataset/VOCdevkit 4/VOC2007/labels"  # ← 指定输出目录
)