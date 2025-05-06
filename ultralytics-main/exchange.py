from pathlib import Path

# 训练集
train_images = list(Path("D:/daima/ultralytics-main/ultralytics/datasets/new/images/val").glob("*.jpg"))
with open("D:/daima/ultralytics-main/ultralytics/datasets/new/labels/train/val.txt", "w") as f:
    f.write("\n".join([f"{img.name}" for img in train_images]))

# 验证集同理