import cv2, datetime
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
from flask_caching import Cache
from push import PUSH
import detect_with_API
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import detect_with_API_person
import torch
from record import ETimer
import random
import xlrd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:happylyq2004922@127.0.0.1:3306/flaskdata'
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column('admin_id', db.Integer, primary_key=True)
    adminname = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
class tongxingjilu_xiaoneirenyuan(db.Model):
    __tablename__ = 'tongxingjilu_xiaoneirenyuan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    shenfen = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    yuanxixinxi = db.Column(db.String(50))
    tongxingshijian = db.Column(db.String(200))
    tongxingweizhi = db.Column(db.String(100))
    tongxingfangshi=db.Column(db.String(100))


class webuser(db.Model):
    __tablename__ = 'webuser'

    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))
    yuanxixinxi = db.Column(db.String(200))
    zhuanye = db.Column(db.String(100))
    nianjibianhao=db.Column(db.String(100))
    banjibianhao=db.Column(db.String(100))

class totaluser(db.Model):
    __tablename__ = 'totaluser'

    id = db.Column('admin_id', db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), default='admin')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class clocation(db.Model):
    __tablename__ = 'clocation'

    id = db.Column('location_id', db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    state = db.Column(db.String(50))
    url = db.Column(db.String(200))


class alarm1(db.Model):
    __tablename__ = 'alarm'

    id = db.Column('alarm_id', db.Integer, primary_key=True)
    chuli = db.Column(db.String(100))
    time = db.Column(db.String(100))
    location = db.Column(db.String(50))
    content = db.Column(db.String(200))

    def to_json(self):
        return {
            'id': self.id,
            'chuli': self.chuli,
            'time': self.time,
            'location': self.location,
            'content': self.content,
        }

class weixianshijianguizepeizhi(db.Model):
    __tablename__ = 'weixianshijianguizepeizhi'

    id = db.Column(db.Integer, primary_key=True)
    guizemingchen = db.Column(db.String(100))
    guizeleixing = db.Column(db.String(100))
    guizemiaoshu = db.Column(db.String(100))

class tongxingjilu_fangkejilu(db.Model):
    __tablename__ = 'tongxingjilu_fangkejilu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    shenfen = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    tongxingshijian = db.Column(db.String(200))
    tongxingweizhi = db.Column(db.String(100))
    tongxingfangshi=db.Column(db.String(100))

class tongxingjilu_neibucheliang(db.Model):
    __tablename__ = 'tongxingjilu_neibucheliang'

    id = db.Column(db.Integer, primary_key=True)
    tongxingcheliang = db.Column(db.String(100))
    chezhuxingming = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    suoshubumen = db.Column(db.String(200))
    tongxingshijian = db.Column(db.String(100))
    tongxingfangxiang=db.Column(db.String(100))
    shebeiweizhi=db.Column(db.String(100))

class tongxingjilu_fangkecheliang(db.Model):
    __tablename__ = 'tongxingjilu_fangkecheliang'

    id = db.Column(db.Integer, primary_key=True)
    tongxingcheliang = db.Column(db.String(100))
    fangkexingming = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    fangwenbumen = db.Column(db.String(200))
    tongxingshijian = db.Column(db.String(100))
    tongxingfangxiang=db.Column(db.String(100))
    shebeiweizhi=db.Column(db.String(100))

class cheliangguanli_cheliangxinxi(db.Model):
    __tablename__ = 'cheliangguanli_cheliangxinxi'

    id = db.Column(db.Integer, primary_key=True)
    chepaihaoma = db.Column(db.String(100))
    chezhuleixing = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    chezhuxingming = db.Column(db.String(50))
    suoshubumen = db.Column(db.String(200))
    cheliangleixing = db.Column(db.String(100))
    cheliangzhuangtai= db.Column(db.String(50))
    shoufeishijian=db.Column(db.String(100))
    jiezhishijian=db.Column(db.String(100))
    beizhu=db.Column(db.String(100))

class cheliangguanli_chezhuxinxi(db.Model):
    __tablename__ = 'cheliangguanli_chezhuxinxi'

    id = db.Column(db.Integer, primary_key=True)
    chezhuxingming = db.Column(db.String(100))
    shoujihao = db.Column(db.String(100))
    xingbie = db.Column(db.String(100))
    chezhuleixing= db.Column(db.String(100))
    suoshubumen = db.Column(db.String(200))
    mingxiacheliang=db.Column(db.String(100))
    beizhu=db.Column(db.String(100))

class cheliangguanli_cheliangheimingdan(db.Model):
    __tablename__ = 'cheliangguanli_cheliangheimingdan'

    id = db.Column(db.Integer, primary_key=True)
    chepaihao = db.Column(db.String(100))
    chezhuxingming = db.Column(db.String(100))
    shoujihao = db.Column(db.String(100))
    cheliangleixing = db.Column(db.String(100))
    suoshubumen = db.Column(db.String(200))
    kaishiriqi=db.Column(db.String(100))
    jieshuriqi=db.Column(db.String(100))
    yuanyin=db.Column(db.String(100))

class fangke_shenqingshenhe(db.Model):
    __tablename__ = 'fangke_shenqingshenhe'

    id = db.Column(db.Integer, primary_key=True)
    fangwenshiyou = db.Column(db.String(100))
    shoufangren = db.Column(db.String(100))
    shenqingren = db.Column(db.String(100))
    shenqingshijian = db.Column(db.String(50))
    fangwenshijian = db.Column(db.String(200))
    suixingrenyuan = db.Column(db.String(100))
    suixingcheliang=db.Column(db.String(100))

class fangke_shenqingjilu(db.Model):
    __tablename__ = 'fangke_shenqingjilu'

    id = db.Column(db.Integer, primary_key=True)
    shenqingbianhao = db.Column(db.String(100))
    fangwenshiyou = db.Column(db.String(100))
    shoufangren = db.Column(db.String(100))
    shenqingren = db.Column(db.String(100))
    shenqingshijian = db.Column(db.String(50))
    fangwenshijian = db.Column(db.String(200))
    suixingrenyuan = db.Column(db.String(100))
    suixingcheliang=db.Column(db.String(100))

class fangke_fangkeliebiao(db.Model):
    __tablename__ = 'fangke_fangkeliebiao'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    state = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))
    beizhu = db.Column(db.String(100))

class fangke_shenherenpeizhi(db.Model):
    __tablename__ = 'fangke_shenherenpeizhi'

    id = db.Column(db.Integer, primary_key=True)
    yuanxixinxi = db.Column(db.String(100))
    shenhefanwei = db.Column(db.String(100))
    name = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    renyuanleixing = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))

class fangke_heimingdanguanli(db.Model):
    __tablename__ = 'fangke_heimingdanguanli'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    state = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))
    yuanyin = db.Column(db.String(100))

class lixiaoweigui1(db.Model):
    __tablename__ = 'lixiaoweigui1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    xuehao = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))
    xueyuan = db.Column(db.String(200))
    zhuanye = db.Column(db.String(100))
    weiguitianshu=db.Column(db.String(100))
    lixiaoshijian=db.Column(db.String(100))

class shijianbaojing_shijianliebiao(db.Model):
    __tablename__ = 'shijianbaojing_shijianliebiao'

    id = db.Column(db.Integer, primary_key=True)
    baojingneirong = db.Column(db.String(100))
    fashengshijian = db.Column(db.String(100))
    zuobiao = db.Column(db.String(100))
    jibie = db.Column(db.String(50))
    shifouchuli = db.Column(db.String(200))

class shijianbaojing_shijianchuliyuan(db.Model):
    __tablename__ = 'shijianbaojing_shijianchuliyuan'

    id = db.Column(db.Integer, primary_key=True)
    shijian = db.Column(db.String(100))
    dengji = db.Column(db.String(100))
    chulibanfa = db.Column(db.String(100))
    zerenren = db.Column(db.String(50))

class sb_gl(db.Model):
    __tablename__ = 'sb_gl'

    id = db.Column(db.Integer, primary_key=True)
    shebeiming = db.Column(db.String(100))
    quyu = db.Column(db.String(100))
    zichanzhuangtai = db.Column(db.String(100))
    shifouzaixian = db.Column(db.String(50))
    zichanleixing = db.Column(db.String(100))
    chuangjianshijian = db.Column(db.String(100))
    baoxiushijian = db.Column(db.String(50))
    ziyuanzhuangtai = db.Column(db.String(50))

class xitongshezhi_kongjianshujuguanli(db.Model):
    __tablename__ = 'xitongshezhi_kongjianshujuguanli'

    id = db.Column(db.Integer, primary_key=True)
    didian = db.Column(db.String(100))
    leixing = db.Column(db.String(100))
    shuoming = db.Column(db.String(100))

class guizepeizhi(db.Model):
    __tablename__ = 'guizepeizhi'

    id = db.Column(db.Integer, primary_key=True)
    guizemingchen = db.Column(db.String(100))
    guizeleixing = db.Column(db.String(100))
    guizemiaoshu = db.Column(db.String(100))




class xitongshezhi_kyonghuguanli(db.Model):
    __tablename__ = 'xitongshezhi_kyonghuguanli'

    id = db.Column(db.Integer, primary_key=True)
    xingming = db.Column(db.String(100))
    xingbie = db.Column(db.String(100))
    dengluzhanghao = db.Column(db.String(100))
    shouji = db.Column(db.String(50))
    xingzhengquyu = db.Column(db.String(100))
    bumen = db.Column(db.String(100))
    juese = db.Column(db.String(50))

class chufaguize(db.Model):
    __tablename__ = 'chufaguize'

    id = db.Column(db.Integer, primary_key=True)
    cfgz = db.Column(db.String(100))
    neirong = db.Column(db.String(100))

class weixianshijianchufaguize(db.Model):
    __tablename__ = 'weixianshijianchufaguize'

    id = db.Column(db.Integer, primary_key=True)
    cfgz = db.Column(db.String(100))
    neirong = db.Column(db.String(100))

class excelchangshi(db.Model):
    __tablename__ = 'excelchangshi'

    id = db.Column(db.Integer, primary_key=True)
    diyilie = db.Column(db.String(100))
    dierlie = db.Column(db.String(100))
    disanlie = db.Column(db.String(100))
    disilie = db.Column(db.String(100))
    diwulie = db.Column(db.String(100))



#a = detect_with_API.detectapi(weights='best_smoke.pt')
# a= detect_with_API_person.detectapi(weights='yolov11s.pt')

conf = 0;


# class VideoCamera():
#     def __init__(self, vurl):
#         # 通过opencv获取实时视频流
#         self.i = 0
#         self.t = 1
#         self.lj = vurl
#         self.video = cv2.VideoCapture(vurl)
#         self.person = 0
#         self.conf = 0
#         self.time1 = ETimer()
#         self.jpeg = 0
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#
#         while self.t:
#             self.i = self.i + 1
#             success, image = self.video.read()
#             if (self.i % 5 == 0):
#                 result, names = a.detect([image])
#                 image = result[0][0]  # 每一帧图片的处理结果图片
#                 ret, self.jpeg = cv2.imencode('.jpg', image)
#
#                 return self.jpeg.tobytes()
#             else:
#                 self.t = 1
#
#     def jiance(self):
#
#         success, image = self.video.read()
#         if success:
#             result, names = a.detect([image])
#             image = result[0][0]
#             for cls, (x1, y1, x2, y2), self.conf in result[0][1]:
#                 print(names[cls], x1, y1, x2, y2, self.conf)  # 识别物体种类、左上角x坐标、左上角y轴坐标、右下角x轴坐标、右下角y轴坐标，置信度
#             if self.conf > 0.4:
#                 with app.app_context():
#                     record_id = 1 + alarm1.query.count()
#                     tempdd = clocation.query.filter_by(url=self.lj).first()
#
#                     sadd = alarm1(id=record_id, time=datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'), chuli="否", location="南区-8教-东南-02",
#                                   content='实验室危险区域')
#                     cv2.imwrite(r"E:\flaskProject24\static\img\\" + str(record_id) + ".jpg", image)
#
#                     db.session.add(sadd)
#                     db.session.commit()
#                     return {
#                         'flag': 1,
#                     }
#             else:
#                 return {
#                     'flag': 0,
#                 }
#         else:
#             return {
#                 'flag': 0,
#             }


tt = 1


@app.route('/ttt1')
def ttt():  # put application's code here

    return render_template("keyInfo.html");

@app.route('/')
@cache.cached(timeout=60)  # Cache for 60 seconds
def index():  # put application's code here
    if (tt == 0):
        """这一块就是说可以通过后台设置的参数来实现对后台执行函数进行判断 """
        return redirect(url_for('houtai'))
    else:
        re1 = alarm1.query.filter_by(chuli='否').all()
        # sum1 = alarm1.query.filter_by(chuli='否').count()
        sum1 = len(re1)

        return render_template("index-v2.html", records1=re1, zxrecords=re1, sum1=sum1)


@app.route('/baojingweb')
def baojingweb():  # 就是找出最新的报警事件 然后把对应那个对象传过去  网页上就显示报警的事件 地点 时间即可

    numall = alarm1.query.count()
    baojingshiti = alarm1.query.filter_by(id=numall).first()
    content = baojingshiti.content
    time = baojingshiti.time
    location = baojingshiti.location
    mingc = '摄像头测试1'
    wu = "无"
    PH = PUSH(content, location, mingc, time, wu)
    PH.push()
    return render_template("baojingweb.html", bj=baojingshiti)


@app.route('/shouye', methods=['GET', 'POST'])
def shouye():  # 就是找出最新的报警事件 然后把对应那个对象传过去  网页上就显示报警的事件 地点 时间即可
    if request.method == 'POST':
        accountname = request.form.get('accountname')
        if accountname == '请输入账号':
            return redirect(url_for('zc'))
        # 这一块实现了表单中的注册一个超链接的跳转的方式
        else:
            password = request.form.get('password')
            og = webuser.query.filter_by(accountname=accountname).first()
            if og.password == password:

                # 下面开始对用户进行登录逻辑的判断

                return redirect(url_for('personalpage'))
            else:
                return render_template("reg.html", msg='密码输入错误')
    else:
        return render_template("reg.html")


@app.route('/personalpage', methods=['GET', 'POST'])
# 这一块来写一个个人主页
def personalpage():
    return render_template("profile-page.html")


@app.route('/zc', methods=['GET', 'POST'])
def zc():
    if request.method == 'POST':
        user_id = 1 + webuser.query.count()
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        obj1 = '学生'
        u1 = webuser(id=user_id, accountname=accountname, password=password, username='', obj1=obj1, obj2=' ',
                     obj3='')
        db.session.add(u1)
        db.session.commit()
        redirect(url_for('shouye'))
    else:
        # 就是说默认是在这个页面的
        return render_template("reg1.html")


@app.route('/change', methods=['GET', 'POST'])
def change_student():
    stu_id = request.args.get('id')

    if request.method == 'POST':
        name = request.form.get('name')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        u1 = webuser.query.filter_by(id=stu_id).first()
        u1.name = name
        u1.chinese = chinese
        u1.math = math
        u1.english = english
        db.session.commit()
        return redirect(url_for('houtai'))
    u1 = webuser.query.filter_by(id=stu_id).first()
    return render_template('change.html', webuser=u1)


@app.route('/new')
def new():  # 这个是写的用户管理的增加
    stu_id = 1 + webuser.query.count()
    new1 = webuser(id=stu_id, accountname='', password='', username='', obj1='', obj2='', obj3='')
    db.session.add(new1)
    """就是说加上一行空白行"""
    db.session.commit()
    return render_template("userMng.html", webusers=webuser.query.all())


@app.route('/new1')
def new1():  # 这个是写报警记录的增加 ----下面的逻辑最后放到外边去就是了
    record_id = 1 + alarm1.query.count()
    new1 = alarm1(id=record_id, time='', location='', content='')
    db.session.add(new1)
    """就是说加上一行空白行"""
    db.session.commit()
    return render_template("record.html", records=alarm1.query.all())


@app.route('/zhuce', methods=['GET', 'POST'])
def zhuce():  # 这个是写报警记录的增加 ----下面的逻辑最后放到外边去就是了

    if request.method == 'POST':
        stu_id = 1 + webuser.query.count()
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        username = request.form.get('username')
        obj1 = request.form.get('obj1')
        obj2 = request.form.get('obj2')
        obj3 = request.form.get('obj3')

        u1 = webuser(id=stu_id, accountname=accountname, password=password, username=username, obj1=obj1, obj2=obj2,
                     obj3=obj3)
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('i1'))
    else:
        return render_template('beifen.html')


@app.route('/dengru', methods=['GET', 'POST'])
def dengru():  # 这个是写报警记录的增加 ----下面的逻辑最后放到外边去就是了

    if request.method == 'POST':

        accountname = request.form.get('accountname')
        password = request.form.get('password')
        user = Admin.query.filter_by(adminname=accountname, password=password).first()
        # og = webuser.query.filter_by(accountname=accountname).first()
        # if og.password == password:
        #     if og.accountname == 'yinjiale1':
        #         return redirect(url_for('houtai'))
        #     else:
        #         return redirect('dengru.html')

        if user:
            # 登录成功，这里可以添加跳转到其他页面的逻辑
            return redirect(url_for('weixianshijianguizepeizhi1'))
        else:
            # 登录失败，返回错误信息
            return render_template('dengru.html', error='账号或密码错误')
    else:
        return render_template('dengru.html')


@app.route('/delete', methods=['GET'])
def delete():  # put application's code here
    stu_id = request.args.get('id')
    """对用户进行删除"""
    u1 = webuser.query.filter_by(id=stu_id).first()
    db.session.delete(u1)
    db.session.commit()
    return redirect(url_for('houtai'))


@app.route('/banyi', methods=['GET'])
def banyi():  # put application's code here
    alarm_id = request.args.get('id')
    """实现对报警事件的转换处理"""
    u1 = alarm1.query.filter_by(id=alarm_id).first()
    u1.chuli = "是"
    db.session.commit()
    return redirect(url_for('i1'))


@app.route('/queren', methods=['GET'])
def quren():  # put application's code here
    alarm_id = request.args.get('id')
    """实现对报警事件的转换处理"""
    u1 = alarm1.query.filter_by(id=alarm_id).first()
    u1.chuli = "是"
    db.session.commit()
    return redirect(url_for('record'))





@app.route('/getwcl', methods=['GET', 'POST'])
def getwcl():
    re5 = alarm1.query.filter_by(chuli='否').all()
    '''所以只要通过rel【1】就可以遍历每一个对象，再把每一个对象加到list里面去就是了  len(re1)这就可以输出对应re1的长度了   然后来一个循环就可以了   '''
    p = 0
    ii = []
    while p < len(re5):
        ad = re5[p].to_json()
        ii.append(ad)
        p = p + 1
    return [len(re5), ii]


@app.route('/getycl', methods=['GET', 'POST'])
def getycl():
    re2 = alarm1.query.filter_by(chuli='是').all()
    '''所以只要通过rel【1】就可以遍历每一个对象，再把每一个对象加到list里面去就是了  len(re1)这就可以输出对应re1的长度了   然后来一个循环就可以了   '''
    p1 = 0
    ii1 = []
    while p1 < len(re2):
        ad1 = re2[p1].to_json()
        ii1.append(ad1)
        p1 = p1 + 1
    return [len(re2), ii1]

#
# @app.route('/xiaoxi', methods=['GET', 'POST'])
# def xiaoxi():
#     re4 = []
#     sum11 = alarm1.query.filter_by(chuli='否').count()
#     zongti = alarm1.query.filter_by(chuli='否').all()
#     print(zongti[0])
#     return [sum11, re4]


# @app.route('/baojing', methods=['GET', 'POST'])
# def baojing():
#     # 这一块就是报警的部分的处理
#     c2 = VideoCamera("http://47.100.107.225:8090/live/111.flv")
#
#     return c2.jiance()


@app.route('/chakan', methods=['GET'])
def chakan():  # put application's code here
    alarm_id = request.args.get('id')
    """对用户进行删除"""
    u1 = alarm1.query.filter_by(id=alarm_id).first()
    db.session.delete(u1)
    db.session.commit()
    return redirect(url_for('record'))


@app.route('/i1')
def i1():  # put application's code here
    re1 = alarm1.query.filter_by(chuli='否').all()
    sum1 = alarm1.query.filter_by(chuli='否').count()
    return render_template("index-v2.html", records1=re1, zxrecords=re1, sum1=sum1)


@app.route('/houtai', methods=['GET', 'POST'])
def houtai():  # put application's code here

    if request.method == 'POST':
        temppp = request.form.get('sel')
        cc = request.form.get('sel1')
        if cc == '用户名':
            return render_template("userMng.html", webusers=webuser.query.filter_by(username=temppp).all())
        else:
            return render_template("userMng.html", webusers=webuser.query.filter_by(accountname=temppp).all())

    else:
        return render_template("userMng.html", webusers=webuser.query.all())


@app.route('/record', methods=['GET', 'POST'])
def record():  # put application's code here
    if request.method == 'POST':
        tempp = request.form.get('ll')
        c = request.form.get('ll1')
        if c == '地段':
            return render_template("record.html", records=alarm1.query.filter_by(location=tempp).all())
        elif c == '报警内容':
            return render_template("record.html", records=alarm1.query.filter_by(content=tempp).all())
        else:
            return render_template("record.html", records=alarm1.query.filter_by(chuli=tempp).all())
    else:
        return render_template("record.html", records=alarm1.query.all())


@app.route('/car')
def car():  # put application's code here
    return render_template("car.html")


@app.route('/sec')
def sec():  # put application's code here
    return render_template("sec.html")


@app.route('/key')
def key():  # put application's code here
    return render_template("keyInfo.html")


@app.route('/ef')
def ef():  # put application's code here
    return render_template("efficiencyAnalysis.html")


@app.route('/chaxun')
def chaxun():  # put application's code here
    re1 = alarm1.query.filter_by(chuli='否').all()
    return render_template("record.html", records=re1)


@app.route('/jiankong')
def jiankong():  # put application's code here

    return render_template("duoshebei.html")


@app.route('/sgshuaxin')
def sgshuaxin():  # put application's code here
    # 对后续所有的事件都对应建立一个json格式来就行 然后对次数排序 最高放0 次高放1
    sjs = alarm1.query.filter(alarm1.content == "person").count()
    sj1 = {
        'type': 'persion',
        'num': sjs,
    }
    # 0位置放事故次数最多的 1位置放事故次数第二多的
    sj = []
    sj.append(sj1)
    return sj



@app.route('/ddshuaxin')
# 第一个传最多次数的 第二个传次多 第三个传第三多（前面三个为json 第一个参数为地点名 第二个参数为次数） 第四个传平均数
def ddshuaxin():  # put application's code here
    # ddds3 = alarm1.query.filter(alarm1.location == "地段3").count() 这个方法要知道 就是用来给某些事件定下查询的次数的
    dds1 = {
        'type': '地段1',
        'num': random.randint(0,10),
    }

    dds2 = {
        'type': '地段2',
        'num': random.randint(0,10),
    }

    dds3 = {
        'type': '地段3',
        'num': 3+alarm1.query.filter_by(location='南区-3教-东南-02').count(),
    }
    dds4 = {
        'type': '地段3',
        'num': random.randint(0, 10),
    }


    dd = []
    dd.append(dds3)


    return dd

@app.route('/bfbxin')
# 这边就写如何实现那个百分比的动态刷新就可以了
def bfbshuaxin():  # put application's code here

    bfb1 = {
        'type': '楼顶',
        'num': random.randint(0,10),
    }

    bfb2 = {
        'type': '吸烟',
        'num': alarm1.query.filter_by(content='吸烟').count(),
    }

    bfb3 = {
        'type': '探出栏杆',
        'num': random.randint(0,10),
    }
    bfb4= {
        'type': '危险动作',
        'num': 2,
    }
    bfb5 = {
        'type': '水边',
        'num': random.randint(0, 10),
    }
    bfb6 = {
        'type': '地面积水',
        'num': random.randint(0, 10),
    }


    bfb = []
    # bfb.append(bfb1)
    bfb.append(bfb2)
    # bfb.append(bfb3)
    # bfb.append(bfb4)
    # bfb.append(bfb5)
    # bfb.append(bfb6)


    return bfb

@app.route('/cllshuaxin')
# 这边就写如何实现那个百分比的动态刷新就可以了
def cllshuaxin():  # put application's code here

    cll1 = {
        'num': random.randint(0,10)
    }

    cll2 = {
        'num':random.randint(0,10)
    }
    cll3 = {
        'num': random.randint(0,10)
    }
    cll4= {
        'num': random.randint(0, 10)
    }
    cll5 = {
        'num': random.randint(0, 10)
    }
    cll6 = {
        'num': random.randint(0, 10)
    }

    cll= []
    cll.append(cll1)
    cll.append(cll2)
    cll.append(cll3)
    cll.append(cll4)
    cll.append(cll5)
    cll.append(cll6)



    return cll


# @app.route('/video1_feed')  # 这个地址返回rtsp视频流响应
# def video1_feed():
#     v1 = VideoCamera("http://47.100.107.225:8090/live/111.flv")
#     return Response(gen1(v1), mimetype='multipart/x-mixed-replace; boundary=frame')


# 这边就是把图片进行了一波组合，形成了最后的视频   路由绑定在video1上面

def gen1(camera):
    while True:
        frame = camera.get_frame()
        """因为就是在这里触发视频的读取的 所以在这边进行值的一个赋值  然后就到主页面里面去对这个数值进行判断 来触发报警和后台数据的存储"""
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @app.route('/video2_feed')  # 这个地址返回rtmp视频流响应
# def video2_feed():
#     v2 = VideoCamera("http://47.100.107.225:8090/live/222.flv")
#     return Response(gen2(v2), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen2(camera):
    while True:
        frame1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')


# @app.route('/video3_feed')  # 这个地址返回rtmp视频流响应
# def video3_feed():
#     v3 = VideoCamera("http://47.100.107.225:8090/live/333.flv")
#     return Response(gen3(v3), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen3(camera):
    while True:
        frame2 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')


@app.route('/xueshenguanli',methods=['GET', 'POST'])  # 这一块对应的学生管理页面
def xueshenguanli():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        yuanxi = request.form.get('yuanxixinxi')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = webuser.query.filter_by(yuanxixinxi=yuanxi).order_by(text('user_id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("xueshenguanli.html",paginate=paginate, pagedata=pagedata)

    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = webuser.query.order_by(text('user_id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("xueshenguanli.html",paginate=paginate, pagedata=pagedata)




@app.route('/jiankongdinwei')  # 这个路由函数来写对应的监控定位网页
def jiankongdinwei():
    alljiankongdian = clocation.query.all()
    sum1 = alarm1.query.filter_by(chuli='否').count()
    re3 = []
    zx1 = alarm1.query.filter_by(id=sum1).first()
    re3.append(zx1)
    zx1 = alarm1.query.filter_by(id=sum1 - 1).first()
    re3.append(zx1)
    zx1 = alarm1.query.filter_by(id=sum1 - 2).first()
    re3.append(zx1)
    zx1 = alarm1.query.filter_by(id=sum1 - 3).first()
    re3.append(zx1)
    zx1 = alarm1.query.filter_by(id=sum1 - 4).first()
    re3.append(zx1)
    return render_template("jiankongdinwei.html", zxrecords=re3, jiankongs=alljiankongdian)


@app.route('/quanbu')
# 这一块对应的是全部
def quanbu():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 15))
    paginate = totaluser.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
    pagedata = paginate.items
    return render_template('quanbu.html',paginate=paginate, pagedata=pagedata)

@app.route('/xiaoneirenyuan')  #这一块就写校内人员
def xiaoneirenyuan():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = tongxingjilu_xiaoneirenyuan.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("xiaoneirenyuan.html",paginate=paginate, pagedata=pagedata)

@app.route('/fangkejilu')  #这一块就写访客记录
def fangkejilu():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = tongxingjilu_fangkejilu.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("fangkejilu.html",paginate=paginate, pagedata=pagedata)

@app.route('/neibucheliang')  #这一块就写内部车辆（√）
def neibucheliang():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = tongxingjilu_neibucheliang.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("neibucheliang.html",paginate=paginate, pagedata=pagedata)

@app.route('/fangkecheliang')  #这一块就写访客车辆
def fangkecheliang():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = tongxingjilu_fangkecheliang.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("fangkecheliang.html",paginate=paginate, pagedata=pagedata)

@app.route('/cheliangxinxi',methods=['GET', 'POST'])  #这一块就写车辆信息
def cheliangxinxi():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        chezhuleixing = request.form.get('chezhuleixing')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = cheliangguanli_cheliangxinxi.query.filter_by(chezhuleixing=chezhuleixing).order_by(text('id')).paginate(page=page, per_page=per_page,error_out=False)
        pagedata = paginate.items
        return render_template("cheliangxinxi.html", paginate=paginate, pagedata=pagedata)
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = cheliangguanli_cheliangxinxi.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("cheliangxinxi.html",paginate=paginate, pagedata=pagedata)

@app.route('/chezhuxinxi')  #这一块就写车主信息
def chezhuxinxi():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = cheliangguanli_chezhuxinxi.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("chezhuxinxi.html",paginate=paginate, pagedata=pagedata)

@app.route('/cheliangheimingdan')  #这一块就写车辆黑名单
def cheliangheimingdan():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = cheliangguanli_cheliangheimingdan.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("cheliangheimingdan.html",paginate=paginate, pagedata=pagedata)

@app.route('/fangkeshengqingshenghe')  #这一块就写访客申请审核
def fangkeshengqingshenghe():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = fangke_shenqingshenhe.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("fangkeshengqingshenghe.html",paginate=paginate, pagedata=pagedata)

@app.route('/fangkeshenqingjilu')  #这一块就写访客记录
def fangkeshenqingjilu():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = fangke_shenqingjilu.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("fangkeshenqingjilu.html",paginate=paginate, pagedata=pagedata)

@app.route('/fangkeliebiao')  #这一块就写访客列表
def fangkeliebiao():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = fangke_fangkeliebiao.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("fangkeliebiao.html",paginate=paginate, pagedata=pagedata)

@app.route('/shenherenpeizhi')  #这一块就写访客审核人配置
def shenherenpeizhi():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = fangke_shenherenpeizhi.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("shenherenpeizhi.html",paginate=paginate, pagedata=pagedata)

@app.route('/heimingdanguanli')  #这一块就写访客黑名单管理
def heimingdanguanli():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = fangke_heimingdanguanli.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("heimingdanguanli.html",paginate=paginate, pagedata=pagedata)

@app.route('/lixiaoweigui')  #这一块就写离校未归
def lixiaoweigui():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = lixiaoweigui1.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("lixiaoweigui.html",paginate=paginate, pagedata=pagedata)

@app.route('/shijianliebiao', methods=['GET', 'POST'])  #这一块就写事件列表
def shijianliebiao():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('shifouchuli')
        jibie = request.form.get('jibie')
        name = request.form.get('213')
        print(name)
        print(jibie)
        if accountname==None:
            accountname='否'
        else:
            accountname = '是'
        if jibie==None:
         page = int(request.args.get('page', 1))
         per_page = int(request.args.get('per_page', 15))
         paginate = shijianbaojing_shijianliebiao.query.filter_by(shifouchuli=accountname).order_by(text('id')).paginate(page=page, per_page=per_page,                                                                           error_out=False)
         pagedata = paginate.items
         return render_template("shijianliebiao.html", paginate=paginate, pagedata=pagedata)
        else:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 15))
            paginate = shijianbaojing_shijianliebiao.query.filter_by(shifouchuli=accountname).filter_by(jibie=jibie).order_by(
                text('id')).paginate(page=page, per_page=per_page, error_out=False)
            pagedata = paginate.items
            return render_template("shijianliebiao.html", paginate=paginate, pagedata=pagedata)

    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = shijianbaojing_shijianliebiao.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("shijianliebiao.html",paginate=paginate, pagedata=pagedata)

@app.route('/shijianchuliyuan')  #这一块就写事件处理预案
def shijianchuliyuan():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = shijianbaojing_shijianchuliyuan.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("shijianchuliyuan.html",paginate=paginate, pagedata=pagedata)

@app.route('/sbgl')  #这一块就写设备管理
def sbgl():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = sb_gl.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("shebeiguanli.html",paginate=paginate, pagedata=pagedata)

@app.route('/kongjianshujuguanli')  #这一块就写空间数据管理
def kongjianshujuguanli():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = xitongshezhi_kongjianshujuguanli.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("kongjianshujuguanli.html",paginate=paginate, pagedata=pagedata)

@app.route('/yonghuguanli')  #这一块就写用户管理
def yonghuguanli():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = xitongshezhi_kyonghuguanli.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("yonghuguanli.html",paginate=paginate, pagedata=pagedata)

@app.route('/cheliangguizepeizhi')  #这一块就写车辆配置配置
def cheliangguizepeizhi():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = guizepeizhi.query.order_by(text('id')).paginate(page=page, per_page=per_page,error_out=False)
        pagedata = paginate.items
        return render_template("cheliangguizepeizhi.html",paginate=paginate, pagedata=pagedata)

@app.route('/weixianquyuhuafen', methods=['GET', 'POST'])  #这一块就写危险区域的划分
def weixianquyuhuafen():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
       return redirect(url_for('weixianquyuhuafen'))

    else:
        return render_template("weixianquyuhuafen.html")

@app.route('/chufaguize1')  #这一块就写处罚规则
def chufaguize1():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = chufaguize.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("chufaguize.html",paginate=paginate, pagedata=pagedata)

@app.route('/weixianshijianchufaguize1')  #这一块就写处罚规则
def weixianshijianchufaguize1():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('i1'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = weixianshijianchufaguize.query.order_by(text('id')).paginate(page=page, per_page=per_page, error_out=False)
        pagedata = paginate.items
        return render_template("weixianshijianchufaguize.html",paginate=paginate, pagedata=pagedata)

@app.route('/shipingjiankong',methods = ['GET','POST'])  #这一块就写视频监控
def shipingjiankong():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        didian = request.form.get('shipingdiduan')
        a='video1_feed'
        b='video2_feed'
        d='video3_feed'
        e = 'video3_feed'
        f = 'video3_feed'
        g = 'video3_feed'
        h = 'video3_feed'
        i = 'video3_feed'
        j = 'video3_feed'
        aa=[]
        c=[]
        c.append(a)
        c.append(b)
        c.append(d)
        c.append(e)
        c.append(f)
        c.append(g)
        aa.append(a)
        aa.append(b)
        aa.append(d)
        aa.append(e)
        aa.append(f)
        aa.append(g)
        c.append(h)
        c.append(i)
        c.append(j)
        if didian == '高铁站台':
            return render_template("shipingjiankong.html",spldz=c)
        else:
            return render_template("shipingjiankong.html", spldz=aa)

    else:
        return render_template("shipingjiankong.html")

@app.route('/exceldaoru',methods = ['GET','POST'])
# 这个来实现excel的导入
def exceldaoru():
    return render_template("exceldaoru.html")# 根据具体问题返回不同内容

@app.route('/toexcel',methods = ['GET','POST'])
# 这个来实现excel的导入
def toExcel():
    if request.method == 'POST':
        file = request.files.get('file')
        f = file.read()
        data_file = xlrd.open_workbook(file_contents=f)
        # sheet1
        table = data_file.sheet_by_index(0)
        # print(table)
        # print(table.nrows) # 获取该sheet中的有效行数
        now=xitongshezhi_kongjianshujuguanli.query.count();
        for row_num in range(1, table.nrows):
            id=now+row_num;
            for cow_num in range(0, table.ncols):
                if cow_num==0:
                    diyilie=table.cell_value(row_num,cow_num)
                if cow_num==1:
                    dierlie = table.cell_value(row_num, cow_num)
                if cow_num == 2:
                    disanlie = table.cell_value(row_num, cow_num)

            nn=xitongshezhi_kongjianshujuguanli(id=id,didian=diyilie,leixing=dierlie,shuoming=disanlie)
            db.session.add(nn)
            db.session.commit()
        return redirect('/kongjianshujuguanli') # 根据具体问题返回不同内容

@app.route('/weixianshijianguizepeizhi1')  #这一块就写危险事件的违章规则
def weixianshijianguizepeizhi1():
    if request.method == 'POST':
        #这一块来写对应的搜索功能的部分
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        og = webuser.query.filter_by(accountname=accountname).first()
        if og.password == password:
            if og.accountname == 'yinjiale1':
                return redirect(url_for('houtai'))
            else:
                return redirect(url_for('index-v2'))
    else:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        paginate = weixianshijianguizepeizhi.query.order_by(text('id')).paginate(page=page, per_page=per_page,error_out=False)
        pagedata = paginate.items
        return render_template("weixianshijianguizepeizhi.html",paginate=paginate, pagedata=pagedata)


@app.route('/userMng')
def userMng():
    return render_template('userMng.html')

@app.route('/shebeiguanli')
def shebeiguanli():
    return render_template('shebeiguanli.html')

@app.route('/xuexi', methods=['GET', 'POST'])
# 这一块来写一个个人主页
def xuexi():
    return render_template("xuexi.html")

@app.route('/tables')
def tables():
    return render_template('tables.html')

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
