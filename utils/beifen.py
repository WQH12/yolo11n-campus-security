while self.t:
    self.i = self.i + 1
    success, image = self.video.read()
    if (self.i % 10 == 0):
        result, names = a.detect([image])
        image = result[0][0]  # 每一帧图片的处理结果图片
        self.conf = 0;
        for cls, (x1, y1, x2, y2), self.conf in result[0][1]:
            print(names[cls], x1, y1, x2, y2, self.conf)  # 识别物体种类、左上角x坐标、左上角y轴坐标、右下角x轴坐标、右下角y轴坐标，置信度
        if (self.conf > 0.4 and self.person == 0):
            self.person = 1
            self.time1.start()
        elif (self.conf < 0.4 and self.person == 1):
            self.person = 0
            self.time1.stop()
            if (self.time1.lasted > 2):  # 这一块具体的时间后面可以继续调就是了
                with app.app_context():
                    print('在危险区域停留超过5秒！')
                    record_id = 1 + alarm1.query.count()
                    tempdd1 = clocation.query.filter_by(url=self.lj).first()
                    sadd = alarm1(id=record_id, time=time.asctime(), chuli="否", location=tempdd1.location,
                                  content='主视频流')
                    cv2.imwrite(r"E:\flaskProject24\static\img\\" + str(record_id) + ".jpg", image)
                    db.session.add(sadd)
                    db.session.commit()
        ret, self.jpeg = cv2.imencode('.jpg', image)

        return self.jpeg.tobytes()
    else:
        self.t = 1