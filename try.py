from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 'yinjiale1'
    database = 'data'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False


# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    type = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    idcard = db.Column(db.String(50))
    yuanxixinxi = db.Column(db.String(200))


class alarm1(db.Model):

   __tablename__ = 'alarm1'
   __table_args__ = (db.Index('ix_alarm_chuli', 'chuli'),)
   id = db.Column('alarm_id', db.Integer, primary_key = True)
   time = db.Column(db.String(100))
   chuli=db.Column(db.String(100))
   location = db.Column(db.String(50))
   content = db.Column(db.String(200))

class clocation(db.Model):

   __tablename__ = 'clocation'

   id = db.Column('location_id', db.Integer, primary_key = True)
   location = db.Column(db.String(50))
   state =db.Column(db.String(50))
   url = db.Column(db.String(200))

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

class guizepeizhi(db.Model):
    __tablename__ = 'guizepeizhi'

    id = db.Column(db.Integer, primary_key=True)
    guizemingchen = db.Column(db.String(100))
    guizeleixing = db.Column(db.String(100))
    guizemiaoshu = db.Column(db.String(100))

class weixianshijianguizepeizhi(db.Model):
    __tablename__ = 'weixianshijianguizepeizhi'

    id = db.Column(db.Integer, primary_key=True)
    guizemingchen = db.Column(db.String(100))
    guizeleixing = db.Column(db.String(100))
    guizemiaoshu = db.Column(db.String(100))

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



if __name__ == '__main__':
    # app.run(debug=True)
    # 创建所有表
 with app.app_context():
    db.create_all()

