import json
from ultralytics import YOLO
import torch


def main():
    torch.cuda.empty_cache()
    # 1. 加载模型
    model = YOLO("yolo11n.pt")  # 使用预训练的YOLOv8n模型

    # 2. 训练模型（Windows建议workers=4或更少）
    model.train(
        data="D:/daima/ultralytics-main/ultralytics/datasets/new.yaml",
        epochs=100,
        imgsz=416,
        batch=8,
        workers=2,  # 关键修改：Windows系统需要减少workers数量
        name="new_train",  # 可选：指定训练结果保存名称
    )


if __name__ == '__main__':
    main()  # 关键修改：必须将主逻辑放在这个块中