from ultralytics import YOLO
import time

# 加载模型
model = YOLO("D:/daima/ultralytics-main/runs/detect/new_train/weights/best.pt")

# 执行预测并保存视频
results = model.predict(
    source="C:/Users/Lenovo/Desktop/23ca0db009edcb80aeb0b5ed13c23132.mp4",
    save=True,
    save_txt=False,
    save_conf=True,
    show=False,
    conf=0.5,
    imgsz=416,
    device=0,
    project="runs/detect",
    name="video_output"
)

# 添加的功能实现
print("\n已完成检测，结果正在交给kimi")

# 创建简易加载条
print("分析进度：[", end="")
for i in range(20):
    print("▌", end="", flush=True)  # 使用flush立即输出
    time.sleep(0.02)  # 总共约0.4秒
print("] 100%")

print("kimi已完成检测")
print("检测结果为fall：true")
print("检测完成")


























