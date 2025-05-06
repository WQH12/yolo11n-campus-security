from ultralytics import YOLO

# 加载最佳权重（推荐）或最后权重
model = YOLO("D:/daima/ultralytics-main/runs/detect/new_train/weights/best.pt")  # 或 last.pt
results = model.predict("C:/Users/Lenovo/Desktop/23ca0db009edcb80aeb0b5ed13c23132.mp4", save=True)  # 结果会保存在 runs/detect/predict/
# 预测所有测试图片并保存结果
#results = model.predict(
#    source="coco2017_test/images/test2017",
#    save=True,          # 保存预测图片
#    save_txt=True,      # 保存预测框为txt文件
#    save_conf=True,     # 保存置信度
#    conf=0.25,          # 置信度阈值
#    iou=0.7,            # IoU阈值
#    project="runs/detect",
#    name="coco_test_predict"  # 结果保存目录
#)
#"C:/Users/Lenovo/Desktop/1595214506200933-1605775243-[]-motorcycle.jpg"