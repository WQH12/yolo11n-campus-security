# import torch
# from numpy import random
# from models.experimental import attempt_load
# from utils.datasets import MyLoadImages
# from utils.general import check_img_size, non_max_suppression, apply_classifier, \
#     scale_coords, set_logging
# from utils.plots import plot_one_box
# from utils.torch_utils import select_device, load_classifier
# import argparse
# import sys
# import time
# from pathlib import Path
#
# import cv2
# import torch
# import torch.backends.cudnn as cudnn
# import numpy as np
#
# FILE = Path(__file__).absolute()
# sys.path.append(FILE.parents[0].as_posix())  # add yolov5/ to path
#
# from models.experimental import attempt_load
# from utils.datasets import LoadStreams, LoadImages
# from utils.general import check_img_size, check_requirements, check_imshow, colorstr, non_max_suppression, \
#     apply_classifier, scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
# from utils.plots import colors, plot_one_box
# from utils.torch_utils import select_device, load_classifier, time_synchronized
#
#
# class simulation_opt:
#     def __init__(self, weights='yolov5s.pt',
#                  img_size=640, conf_thres=0.25,
#                  iou_thres=0.45, device='cpu', view_img=False,
#                  classes=None, agnostic_nms=False,
#                  augment=False, update=False, exist_ok=False):
#         self.weights = weights
#         self.source = None
#         self.img_size = img_size
#         self.conf_thres = conf_thres
#         self.iou_thres = iou_thres
#         self.device = device
#         self.view_img = view_img
#         self.classes = classes
#         self.agnostic_nms = agnostic_nms
#         self.augment = augment
#         self.update = update
#         self.exist_ok = exist_ok
#
#
# class detectapi:
#     def __init__(self, weights, img_size=640):
#         self.opt = simulation_opt(weights=weights, img_size=img_size)
#         weights, imgsz = self.opt.weights, self.opt.img_size
#
#         # Initialize
#         set_logging()
#         self.device = select_device(self.opt.device)
#         self.half = self.device.type != 'cpu'  # half precision only supported on CUDA
#
#         # Load model
#         self.model = attempt_load(weights, map_location=self.device)  # load FP32 model
#         self.stride = int(self.model.stride.max())  # model stride
#         self.imgsz = check_img_size(imgsz, s=self.stride)  # check img_size
#
#         if self.half:
#             self.model.half()  # to FP16
#
#         # Second-stage classifier
#         self.classify = False
#         if self.classify:
#             self.modelc = load_classifier(name='resnet101', n=2)  # initialize
#             self.modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=self.device)['model']).to(
#                 self.device).eval()
#
#         # read names and colors
#         self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
#         self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in self.names]
#
#     def detect(self, source):  # 使用时，调用这个函数
#         if type(source) != list:
#             raise TypeError('source must be a list which contain  pictures read by cv2')
#         dataset = MyLoadImages(source, img_size=self.imgsz, stride=self.stride)  # imgsz
#         # 原来是通过路径加载数据集的，现在source里面就是加载好的图片，所以数据集对象的实现要
#         # 重写。修改代码后附。在utils.dataset.py上修改。
#
#         # Run inference
#         if self.device.type != 'cpu':
#             self.model(torch.zeros(1, 3, self.imgsz, self.imgsz).to(self.device).type_as(
#                 next(self.model.parameters())))  # run once
#         # t0 = time.time()
#         result = []
#         '''
#         for path, img, im0s, vid_cap in dataset:'''
#
#         for img, im0s in dataset:
#             # mask for certain region
#             # 1,2,3,4 分别对应左上，右上，右下，左下四个点
#             hl1 = 0 / 10  # 监测区域高度距离图片顶部比例
#             wl1 = 0 / 10  # 监测区域高度距离图片左部比例
#             hl2 = 0 / 10  # 监测区域高度距离图片顶部比例
#             wl2 = 10 / 10  # 监测区域高度距离图片左部比例
#             hl3 = 10 / 10  # 监测区域高度距离图片顶部比例
#             wl3 = 10 / 10  # 监测区域高度距离图片左部比例
#             hl4 = 10 / 10  # 监测区域高度距离图片顶部比例
#             wl4 = 0 / 10  # 监测区域高度距离图片左部比例
#
#             mask = np.zeros([img.shape[1], img.shape[2]], dtype=np.uint8)
#             # mask[round(img.shape[1] * hl1):img.shape[1], round(img.shape[2] * wl1):img.shape[2]] = 255
#             pts = np.array([[int(img.shape[2] * wl1), int(img.shape[1] * hl1)],  # pts1
#                             [int(img.shape[2] * wl2), int(img.shape[1] * hl2)],  # pts2
#                             [int(img.shape[2] * wl3), int(img.shape[1] * hl3)],  # pts3
#                             [int(img.shape[2] * wl4), int(img.shape[1] * hl4)]], np.int32)
#             mask = cv2.fillPoly(mask, [pts], (255, 255, 255))
#             img = img.transpose((1, 2, 0))
#             img = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)
#             img = img.transpose((2, 0, 1))
#
#             img = torch.from_numpy(img).to(self.device)
#             img = img.half() if self.half else img.float()  # uint8 to fp16/32
#             img /= 255.0  # 0 - 255 to 0.0 - 1.0
#             if img.ndimension() == 3:
#                 img = img.unsqueeze(0)
#
#             # Inference
#             # t1 = time_synchronized()
#             pred = self.model(img, augment=self.opt.augment)[0]
#
#             # Apply NMS
#             pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes,
#                                        agnostic=self.opt.agnostic_nms)
#             # t2 = time_synchronized()
#
#             # Apply Classifier
#             if self.classify:
#                 pred = apply_classifier(pred, self.modelc, img, im0s)
#                 # Print time (inference + NMS)
#                 # print(f'{s}Done. ({t2 - t1:.3f}s)')
#                 # Process detections
#
#             det = pred[0]  # 原来的情况是要保持图片，因此多了很多关于保持路径上的处理。另外，pred
#             # 其实是个列表。元素个数为batch_size。由于对于我这个api，每次只处理一个图片，
#             # 所以pred中只有一个元素，直接取出来就行，不用for循环。
#             im0 = im0s.copy()  # 这是原图片，与被传进来的图片是同地址的，需要copy一个副本，否则，原来的图片会受到影响
#             # s += '%gx%g ' % img.shape[2:]  # print string
#             # gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
#             result_txt = []
#             # 对于一张图片，可能有多个可被检测的目标。所以结果标签也可能有多个。
#             # 每被检测出一个物体，result_txt的长度就加一。result_txt中的每个元素是个列表，记录着
#             # 被检测物的类别引索，在图片上的位置，以及置信度
#             for i, det in enumerate(pred):  # detections per image
#                 cv2.putText(im0, "Detection_Region", (int(im0.shape[1] * wl1 - 5), int(im0.shape[0] * hl1 - 5)),
#                             cv2.FONT_HERSHEY_SIMPLEX,
#                             1.0, (255, 255, 0), 2, cv2.LINE_AA)
#                 pts = np.array([[int(im0.shape[1] * wl1), int(im0.shape[0] * hl1)],  # pts1
#                                 [int(im0.shape[1] * wl2), int(im0.shape[0] * hl2)],  # pts2
#                                 [int(im0.shape[1] * wl3), int(im0.shape[0] * hl3)],  # pts3
#                                 [int(im0.shape[1] * wl4), int(im0.shape[0] * hl4)]], np.int32)  # pts4
#                 # pts = pts.reshape((-1, 1, 2))
#                 zeros = np.zeros((im0.shape), dtype=np.uint8)
#                 mask = cv2.fillPoly(zeros, [pts], color=(0, 165, 255))
#                 im0 = cv2.addWeighted(im0, 1, mask, 0.2, 0)
#
#                 cv2.polylines(im0, [pts], True, (255, 255, 0), 3)
#
#             if len(det):
#                 # Rescale boxes from img_size to im0 size
#                 det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
#                 # Write results
#
#                 for *xyxy, conf, cls in reversed(det):
#                     # xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
#                     line = (int(cls.item()), [int(_.item()) for _ in xyxy], conf.item())  # label format
#                     result_txt.append(line)
#                     label = f'{self.names[int(cls)]} {conf:.2f}'
#                     if self.names[int(cls)] == 'person':
#                         plot_one_box(xyxy, im0, label=label, line_thickness=3)
#             result.append((im0, result_txt))  # 对于每张图片，返回画完框的图片，以及该图片的标签列表。
#         return result, self.names
import torch
from numpy import random
from models.experimental import attempt_load
from utils.datasets import MyLoadImages
from utils.general import check_img_size, non_max_suppression, apply_classifier, \
    scale_coords, set_logging
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier
import argparse
import sys
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
import numpy as np
FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[0].as_posix())  # add yolov5/ to path

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, colorstr, non_max_suppression, \
    apply_classifier, scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized



class simulation_opt:
    def __init__(self, weights='yolov5s.pt',
                 img_size=640, conf_thres=0.25,
                 iou_thres=0.45, device='0', view_img=False,
                 classes=None, agnostic_nms=False,
                 augment=False, update=False, exist_ok=False):
        self.weights = weights
        self.source = None
        self.img_size = img_size
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.device = device
        self.view_img = view_img
        self.classes = classes
        self.agnostic_nms = agnostic_nms
        self.augment = augment
        self.update = update
        self.exist_ok = exist_ok


class detectapi:
    def __init__(self, weights, img_size=640):
        self.opt = simulation_opt(weights=weights, img_size=img_size)
        weights, imgsz = self.opt.weights, self.opt.img_size

        # Initialize
        set_logging()
        self.device = select_device(self.opt.device)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        self.model = attempt_load(weights, map_location=self.device)  # load FP32 model
        self.stride = int(self.model.stride.max())  # model stride
        self.imgsz = check_img_size(imgsz, s=self.stride)  # check img_size

        if self.half:
            self.model.half()  # to FP16

        # Second-stage classifier
        self.classify = False
        if self.classify:
            self.modelc = load_classifier(name='resnet101', n=2)  # initialize
            self.modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=self.device)['model']).to(
                self.device).eval()

        # read names and colors
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in self.names]

    def detect(self, source):  # 使用时，调用这个函数
        if type(source) != list:
            raise TypeError('source must be a list which contain  pictures read by cv2')
        dataset = MyLoadImages(source, img_size=self.imgsz, stride=self.stride)  # imgsz
        # 原来是通过路径加载数据集的，现在source里面就是加载好的图片，所以数据集对象的实现要
        # 重写。修改代码后附。在utils.dataset.py上修改。

        # Run inference
        if self.device.type != 'cpu':
            self.model(torch.zeros(1, 3, self.imgsz, self.imgsz).to(self.device).type_as(
                next(self.model.parameters())))  # run once
        # t0 = time.time()
        result = []
        '''
        for path, img, im0s, vid_cap in dataset:'''

        for img, im0s in dataset:
            img1=img
            # mask for certain region
            # 1,2,3,4 分别对应左上，右上，右下，左下四个点
            hl1 = 0/ 10  # 监测区域高度距离图片顶部比例
            wl1 = 0 / 10  # 监测区域高度距离图片左部比例
            hl2 = 0 / 10  # 监测区域高度距离图片顶部比例
            wl2 = 0 / 10  # 监测区域高度距离图片左部比例
            hl3 = 0/10  # 监测区域高度距离图片顶部比例
            wl3 = 0 / 10  # 监测区域高度距离图片左部比例
            hl4 = 0/ 10  # 监测区域高度距离图片顶部比例
            wl4 = 0 / 10  # 监测区域高度距离图片左部比例

            mask = np.zeros([img.shape[1], img.shape[2]], dtype=np.uint8)
                # mask[round(img.shape[1] * hl1):img.shape[1], round(img.shape[2] * wl1):img.shape[2]] = 255
            pts = np.array([[int(img.shape[2] * wl1), int(img.shape[1] * hl1)],  # pts1
                                [int(img.shape[2] * wl2), int(img.shape[1] * hl2)],  # pts2
                                [int(img.shape[2] * wl3), int(img.shape[1] * hl3)],  # pts3
                                [int(img.shape[2] * wl4), int(img.shape[1] * hl4)]], np.int32)
            mask = cv2.fillPoly(mask, [pts], (255, 255, 255))
            img = img.transpose((1, 2, 0))
            img = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)
            img = img.transpose((2, 0, 1))
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            img1 = img1.transpose((1, 2, 0))
            img1 = img1.transpose((2, 0, 1))
            img1 = torch.from_numpy(img1).to(self.device)
            img1 = img1.half() if self.half else img1.float()  # uint8 to fp16/32
            img1 /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img1.ndimension() == 3:
                img1 = img1.unsqueeze(0)
            # Inference
            # t1 = time_synchronized()
            pred = self.model(img, augment=self.opt.augment)[0]
            pred1 = self.model(img1, augment=self.opt.augment)[0]
            # Apply NMS
            pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes,
                                       agnostic=self.opt.agnostic_nms)
            pred1 = non_max_suppression(pred1, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes,
                                       agnostic=self.opt.agnostic_nms)
            # t2 = time_synchronized()

            # Apply Classifier
            if self.classify:
                pred = apply_classifier(pred, self.modelc, img, im0s)
                pred1 = apply_classifier(pred, self.modelc, img1, im0s)
                # Print time (inference + NMS)
                # print(f'{s}Done. ({t2 - t1:.3f}s)')
                # Process detections

            det = pred[0]  # 原来的情况是要保持图片，因此多了很多关于保持路径上的处理。另外，pred
            # 其实是个列表。元素个数为batch_size。由于对于我这个api，每次只处理一个图片，
            # 所以pred中只有一个元素，直接取出来就行，不用for循环。
            det1 = pred1[0]
            im0 = im0s.copy()  # 这是原图片，与被传进来的图片是同地址的，需要copy一个副本，否则，原来的图片会受到影响
            # s += '%gx%g ' % img.shape[2:]  # print string
            # gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            im1 = im0s.copy()
            result_txt = []
            # 对于一张图片，可能有多个可被检测的目标。所以结果标签也可能有多个。
            # 每被检测出一个物体，result_txt的长度就加一。result_txt中的每个元素是个列表，记录着
            # 被检测物的类别引索，在图片上的位置，以及置信度

            # for i, det in enumerate(pred):  # detections per image
            #     cv2.putText(im0, "Detection_Region", (int(im0.shape[1] * wl1 - 5), int(im0.shape[0] * hl1 - 5)),
            #                     cv2.FONT_HERSHEY_SIMPLEX,
            #                     1.0, (255, 255, 0), 2, cv2.LINE_AA)
            #     pts = np.array([[int(im0.shape[1] * wl1), int(im0.shape[0] * hl1)],  # pts1
            #                         [int(im0.shape[1] * wl2), int(im0.shape[0] * hl2)],  # pts2
            #                         [int(im0.shape[1] * wl3), int(im0.shape[0] * hl3)],  # pts3
            #                         [int(im0.shape[1] * wl4), int(im0.shape[0] * hl4)]], np.int32)  # pts4
            #         # pts = pts.reshape((-1, 1, 2))
            #     zeros = np.zeros((im0.shape), dtype=np.uint8)
            #     mask = cv2.fillPoly(zeros, [pts], color=(0, 165, 255))
            #     im0 = cv2.addWeighted(im0, 1, mask, 0.2, 0)
            #
            #     cv2.polylines(im0, [pts], True, (255, 255, 0), 3)




            if len(det1):
                det1[:, :4] = scale_coords(img1.shape[2:], det1[:, :4], im1.shape).round()
                for *xy, conf, cls in reversed(det1):
                    # xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    line = (int(cls.item()), [int(_.item()) for _ in xy], conf.item())  # label format
                    result_txt.append(line)
                    label = f'{self.names[int(cls)]}'
                    if self.names[int(cls)] == 'person':
                     plot_one_box(xy, im0, label=label, color = (0,255,0), line_thickness=2)
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                # Write results

                for *xyxy, conf, cls in reversed(det):
                    # xywh = (xyxy2xywh(torch.++
                    # tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    line = (int(cls.item()), [int(_.item()) for _ in xyxy], conf.item())  # label format
                    result_txt.append(line)
                    if self.names[int(cls)] == 'person':
                     plot_one_box(xyxy, im0, label='WARNING',line_thickness=4)

            result.append((im0, result_txt))  # 对于每张图片，返回画完框的图片，以及该图片的标签列表。
        return result, self.names