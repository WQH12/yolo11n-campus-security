# import cv2
# import detect_with_API
# import detect_with_API_person
# import torch
# from record import ETimer
# person=0
# cap = cv2.VideoCapture('duorenyuan.mp4')  # 0
# #a = detect_with_API.detectapi(weights='best_fire.pt')
# a = detect_with_API_person.detectapi(weights='yolov5s.pt')
# time1=ETimer()
# if __name__ == '__main__':
#     with torch.no_grad():
#         while True:
#             rec, img = cap.read()
#             result, names = a.detect([img])
#             img = result[0][0]  # 每一帧图片的处理结果图片
#             # 每一帧图像的识别结果（可包含多个物体）
#             conf=0
#             for cls, (x1, y1, x2, y2), conf in result[0][1]:
#                 print(names[cls], x1, y1, x2, y2, conf)  # 识别物体种类、左上角x坐标、左上角y轴坐标、右下角x轴坐标、右下角y轴坐标，置信度
#                 '''
#                 cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
#                 cv2.putText(img,names[cls],(x1,y1-20),cv2.FONT_HERSHEY_DUPLEX,1.5,(255,0,0))'''
#             if(conf>0.4 and person==0):
#                 person=1
#                 time1.start()
#             elif(conf<0.4 and person==1):
#                 person=0
#                 time1.stop()
#                 if(time1.lasted>20):
#                  print('在危险区域停留超过20秒！')  # 将每一帧的结果输出分开
#             cv2.imshow("vedio", img)
#
#             if cv2.waitKey(1) == ord('q'):
#                 break
import cv2
import detect_with_API
import detect_with_API_person
import torch

cap = cv2.VideoCapture('ruqinhuangxian1.mp4')  # 0
a = detect_with_API_person.detectapi(weights='yolov5s.pt')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# 设置视频帧频
fps = cap.get(cv2.CAP_PROP_FPS)
# 设置视频大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('jianceruqinhuangxian2.mp4',fourcc ,fps, size)
if __name__ == '__main__':
    with torch.no_grad():
        while True:
            rec, img = cap.read()
            result, names = a.detect([img])
            img = result[0][0]  # 每一帧图片的处理结果图片
            # 每一帧图像的识别结果（可包含多个物体）
            for cls, (x1, y1, x2, y2), conf in result[0][1]:
                print(names[cls], x1, y1, x2, y2, conf)  # 识别物体种类、左上角x坐标、左上角y轴坐标、右下角x轴坐标、右下角y轴坐标，置信度
                '''
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
                cv2.putText(img,names[cls],(x1,y1-20),cv2.FONT_HERSHEY_DUPLEX,1.5,(255,0,0))'''
            print()  # 将每一帧的结果输出分开
            cv2.imshow("vedio", img)

            out.write(img)
            if cv2.waitKey(1) == ord('q'):
                break