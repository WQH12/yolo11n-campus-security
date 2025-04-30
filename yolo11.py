import json
from ultralytics import YOLO
import torch


def main():
    torch.cuda.empty_cache()
    # 1. 加载模型
    model = YOLO("D:/daima/ultralytics-main/runs/detect/coco_train2/weights/last.pt")  

    # 2. 训练模型（Windows建议workers=4或更少）
    model.train(
        data="D:/daima/ultralytics-main/ultralytics/datasets/coco.yaml",
        epochs=100,
        imgsz=416,
        batch=8,
        workers=2,  # 关键修改：Windows系统需要减少workers数量
        name="coco_train",  # 可选：指定训练结果保存名称
        resume=True  # 如果需要恢复
    )

    # 3. 用训练好的模型进行推理
    results = model("D:/daima/ultralytics-main/ultralytics/datasets/coco/images/test2017/000000000001.jpg")

    # 4. 处理结果（例如显示或保存）
    results[0].show()  # 显示预测结果
    results[0].save("prediction.jpg")  # 保存预测结果


if __name__ == '__main__':
    main()  # 关键修改：必须将主逻辑放在这个块中