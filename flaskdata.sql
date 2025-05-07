-- 创建数据库
-- CREATE DATABASE flaskdata;
USE flaskdata;
-- 建表语句
CREATE TABLE IF NOT EXISTS tongxingjilu_xiaoneirenyuan(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    shenfen VARCHAR(100),
    phone VARCHAR(100),
    yuanxixinxi VARCHAR(50),
    tongxingshijian VARCHAR(200),
    tongxingweizhi VARCHAR(100),
    tongxingfangshi VARCHAR(100)
);
-- 测试数据插入
INSERT INTO tongxingjilu_xiaoneirenyuan (name, shenfen, phone, yuanxixinxi, tongxingshijian, tongxingweizhi, tongxingfangshi)
VALUES ('张三', '学生', '13812345678', '计算机学院', '2025-04-20 10:00', '教学楼A座', '步行');

-- 建表语句
CREATE TABLE  IF NOT EXISTS webuser (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    sex VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50),
    yuanxixinxi VARCHAR(200),
    zhuanye VARCHAR(100),
    nianjibianhao VARCHAR(100),
    banjibianhao VARCHAR(100)
);
-- 测试数据插入
INSERT INTO webuser (name, sex, phone, idcard, yuanxixinxi, zhuanye, nianjibianhao, banjibianhao)
VALUES ('李四', '男', '13987654321', '110101200001011234', '软件学院', '软件工程', '2023级', '2班');


-- 建表语句
CREATE TABLE  IF NOT EXISTS totaluser (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    sex VARCHAR(100),
    type VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50),
    yuanxixinxi VARCHAR(200)
);
-- 测试数据插入
INSERT INTO totaluser (name, sex, type, phone, idcard, yuanxixinxi)
VALUES ('王五', '女', '教师', '15845678901', '120102198502024567', '管理学院');

-- 建表语句
CREATE TABLE  IF NOT EXISTS clocation (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    url VARCHAR(200)
);
-- 测试数据插入
INSERT INTO clocation (location, state, url)
VALUES ('图书馆', '正常', 'http://lib.example.com');

-- 建表语句（注意表名与模型中的 __tablename__ 一致为 'alarm'）
CREATE TABLE  IF NOT EXISTS alarm (
    alarm_id INT PRIMARY KEY AUTO_INCREMENT,
    chuli VARCHAR(100),
    time VARCHAR(100) NOT NULL,
    location VARCHAR(50) NOT NULL,
    content VARCHAR(200)
);
-- 测试数据插入
INSERT INTO alarm (chuli, time, location, content)
VALUES ('未处理', '2025-04-20 14:30', '操场', '异常人员聚集');
INSERT INTO flaskdata.alarm (chuli, time, location, content)
VALUES 
('否', '2025-04-20 10:00:00', '地点A', '测试报警内容1'),
('是', '2025-04-20 11:00:00', '地点B', '测试报警内容2'),
('否', '2025-04-20 12:00:00', '地点C', '测试报警内容3');


-- 建表语句
CREATE TABLE  IF NOT EXISTS weixianshijianguizepeizhi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    guizemingchen VARCHAR(100) NOT NULL,
    guizeleixing VARCHAR(100),
    guizemiaoshu VARCHAR(100)
);
-- 测试数据插入
INSERT INTO weixianshijianguizepeizhi (guizemingchen, guizeleixing, guizemiaoshu)
VALUES ('安全检查规则', '人员管理', '每日进出登记');

-- 建表语句
CREATE TABLE  IF NOT EXISTS tongxingjilu_fangkejilu (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    shenfen VARCHAR(100),
    phone VARCHAR(100),
    tongxingshijian VARCHAR(200),
    tongxingweizhi VARCHAR(100),
    tongxingfangshi VARCHAR(100)
);
-- 测试数据插入
INSERT INTO tongxingjilu_fangkejilu (name, shenfen, phone, tongxingshijian, tongxingweizhi, tongxingfangshi)
VALUES ('访客A', '客户', '18611112222', '2025-04-20 09:30', '行政楼', '自驾');

-- 建表语句
CREATE TABLE  IF NOT EXISTS tongxingjilu_neibucheliang (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tongxingcheliang VARCHAR(100) NOT NULL,
    chezhuxingming VARCHAR(100),
    phone VARCHAR(100),
    suoshubumen VARCHAR(200),
    tongxingshijian VARCHAR(100),
    tongxingfangxiang VARCHAR(100),
    shebeiweizhi VARCHAR(100)
);
-- 测试数据插入
INSERT INTO tongxingjilu_neibucheliang (tongxingcheliang, chezhuxingming, phone, suoshubumen, tongxingshijian, tongxingfangxiang, shebeiweizhi)
VALUES ('京A12345', '赵六', '13598765432', '后勤部', '2025-04-20 11:00', '东门进', '停车场B区');

-- 建表语句
CREATE TABLE  IF NOT EXISTS tongxingjilu_fangkecheliang (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tongxingcheliang VARCHAR(100) NOT NULL,
    fangkexingming VARCHAR(100),
    phone VARCHAR(100),
    fangwenbumen VARCHAR(200),
    tongxingshijian VARCHAR(100),
    tongxingfangxiang VARCHAR(100),
    shebeiweizhi VARCHAR(100)
);
-- 测试数据插入
INSERT INTO tongxingjilu_fangkecheliang (tongxingcheliang, fangkexingming, phone, fangwenbumen, tongxingshijian, tongxingfangxiang, shebeiweizhi)
VALUES ('沪B67890', '访客B', '17788889999', '技术部', '2025-04-20 14:00', '西门进', '临时停车区');

-- 建表语句
CREATE TABLE  IF NOT EXISTS cheliangguanli_cheliangxinxi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    chepaihaoma VARCHAR(100) NOT NULL,
    chezhuleixing VARCHAR(100),
    phone VARCHAR(100),
    chezhuxingming VARCHAR(50),
    suoshubumen VARCHAR(200),
    cheliangleixing VARCHAR(100),
    cheliangzhuangtai VARCHAR(50),
    shoufeishijian VARCHAR(100),
    jiezhishijian VARCHAR(100),
    beizhu VARCHAR(100)
);
-- 测试数据插入
INSERT INTO cheliangguanli_cheliangxinxi (chepaihaoma, chezhuleixing, phone, chezhuxingming, suoshubumen, cheliangleixing, cheliangzhuangtai, shoufeishijian, jiezhishijian, beizhu)
VALUES ('粤C11223', '员工', '13722223333', '钱七', '研发部', '轿车', '正常', '2025-01-01', '2025-12-31', '年度保养');

-- 建表语句
CREATE TABLE  IF NOT EXISTS cheliangguanli_chezhuxinxi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    chezhuxingming VARCHAR(100) NOT NULL,
    shoujihao VARCHAR(100),
    xingbie VARCHAR(100),
    chezhuleixing VARCHAR(100),
    suoshubumen VARCHAR(200),
    mingxiacheliang VARCHAR(100),
    beizhu VARCHAR(100)
);
-- 测试数据插入
INSERT INTO cheliangguanli_chezhuxinxi (chezhuxingming, shoujihao, xingbie, chezhuleixing, suoshubumen, mingxiacheliang, beizhu)
VALUES ('孙八', '15933334444', '男', '管理层', '行政部', '奥迪A6', '备用车辆');

-- 建表语句
CREATE TABLE  IF NOT EXISTS cheliangguanli_cheliangheimingdan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    chepaihao VARCHAR(100) NOT NULL,
    chezhuxingming VARCHAR(100),
    shoujihao VARCHAR(100),
    cheliangleixing VARCHAR(100),
    suoshubumen VARCHAR(200),
    kaishiriqi VARCHAR(100),
    jieshuriqi VARCHAR(100),
    yuanyin VARCHAR(100)
);
-- 测试数据插入
INSERT INTO cheliangguanli_cheliangheimingdan (chepaihao, chezhuxingming, shoujihao, cheliangleixing, suoshubumen, kaishiriqi, jieshuriqi, yuanyin)
VALUES ('黑A99887', '违规车辆', '18855556666', '货车', '外部单位', '2025-04-01', '2025-04-30', '多次违规停放');

-- 建表语句
CREATE TABLE  IF NOT EXISTS fangke_shenqingshenhe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fangwenshiyou VARCHAR(100) NOT NULL,
    shoufangren VARCHAR(100),
    shenqingren VARCHAR(100),
    shenqingshijian VARCHAR(50),
    fangwenshijian VARCHAR(200),
    suixingrenyuan VARCHAR(100),
    suixingcheliang VARCHAR(100)
);
-- 测试数据插入
INSERT INTO fangke_shenqingshenhe (fangwenshiyou, shoufangren, shenqingren, shenqingshijian, fangwenshijian, suixingrenyuan, suixingcheliang)
VALUES ('商务合作', '李经理', '王秘书', '2025-04-19 15:00', '2025-04-20 14:00', '2人', '无');

-- 建表语句
CREATE TABLE  IF NOT EXISTS fangke_shenqingjilu (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shenqingbianhao VARCHAR(100) NOT NULL,
    fangwenshiyou VARCHAR(100),
    shoufangren VARCHAR(100),
    shenqingren VARCHAR(100),
    shenqingshijian VARCHAR(50),
    fangwenshijian VARCHAR(200),
    suixingrenyuan VARCHAR(100),
    suixingcheliang VARCHAR(100)
);
-- 测试数据插入
INSERT INTO fangke_shenqingjilu (shenqingbianhao, fangwenshiyou, shoufangren, shenqingren, shenqingshijian, fangwenshijian, suixingrenyuan, suixingcheliang)
VALUES ('FK20250420001', '参观交流', '张主管', '赵助理', '2025-04-18 10:00', '2025-04-20 10:30', '3人', '客车');

-- 建表语句
CREATE TABLE  IF NOT EXISTS fangke_fangkeliebiao (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    sex VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50),
    beizhu VARCHAR(100)
);
-- 测试数据插入
INSERT INTO fangke_fangkeliebiao (name, state, sex, phone, idcard, beizhu)
VALUES ('访客C', '已登记', '女', '18977778888', '310103199503036789', '预约访客');

-- 建表语句
CREATE TABLE  IF NOT EXISTS fangke_shenherenpeizhi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    yuanxixinxi VARCHAR(100) NOT NULL,
    shenhefanwei VARCHAR(100),
    name VARCHAR(100),
    sex VARCHAR(100),
    renyuanleixing VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50)
);
-- 测试数据插入
INSERT INTO fangke_shenherenpeizhi (yuanxixinxi, shenhefanwei, name, sex, renyuanleixing, phone, idcard)
VALUES ('技术部', '部门访客', '周九', '男', '审核员', '13366667777', '440304198004041234');

-- 建表语句
CREATE TABLE  IF NOT EXISTS fangke_heimingdanguanli (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    sex VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50),
    yuanyin VARCHAR(100)
);
-- 测试数据插入
INSERT INTO fangke_heimingdanguanli (name, state, sex, phone, idcard, yuanyin)
VALUES ('黑名单人员', '禁用', '男', '14722223333', '110105197505055678', '多次骚扰');

-- 建表语句
CREATE TABLE  IF NOT EXISTS lixiaoweigui1 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    xuehao VARCHAR(100),
    phone VARCHAR(100),
    idcard VARCHAR(50),
    xueyuan VARCHAR(200),
    zhuanye VARCHAR(100),
    weiguitianshu VARCHAR(100),
    lixiaoshijian VARCHAR(100)
);
-- 测试数据插入
INSERT INTO lixiaoweigui1 (name, xuehao, phone, idcard, xueyuan, zhuanye, weiguitianshu, lixiaoshijian)
VALUES ('违纪学生', '20230001', '15088889999', '320106200506069012', '文学院', '汉语言文学', '3天', '2025-04-15');

-- 建表语句
CREATE TABLE  IF NOT EXISTS shijianbaojing_shijianliebiao (
    id INT PRIMARY KEY AUTO_INCREMENT,
    baojingneirong VARCHAR(100) NOT NULL,
    fashengshijian VARCHAR(100),
    zuobiao VARCHAR(100),
    jibie VARCHAR(50),
    shifouchuli VARCHAR(200)
);
-- 测试数据插入
INSERT INTO shijianbaojing_shijianliebiao (baojingneirong, fashengshijian, zuobiao, jibie, shifouchuli)
VALUES ('消防报警', '2025-04-20 15:00', '宿舍楼302', '一级', '待处理');

-- 建表语句
CREATE TABLE  IF NOT EXISTS shijianbaojing_shijianchuliyuan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shijian VARCHAR(100) NOT NULL,
    dengji VARCHAR(100),
    chulibanfa VARCHAR(100),
    zerenren VARCHAR(50)
);
-- 测试数据插入
INSERT INTO shijianbaojing_shijianchuliyuan (shijian, dengji, chulibanfa, zerenren)
VALUES ('消防报警事件', '一级', '启动应急预案', '安保部张主任');

-- 建表语句
CREATE TABLE  IF NOT EXISTS sb_gl (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shebeiming VARCHAR(100) NOT NULL,
    quyu VARCHAR(100),
    zichanzhuangtai VARCHAR(100),
    shifouzaixian VARCHAR(50),
    zichanleixing VARCHAR(100),
    chuangjianshijian VARCHAR(100),
    baoxiushijian VARCHAR(50),
    ziyuanzhuangtai VARCHAR(50)
);
-- 测试数据插入
INSERT INTO sb_gl (shebeiming, quyu, zichanzhuangtai, shifouzaixian, zichanleixing, chuangjianshijian, baoxiushijian, ziyuanzhuangtai)
VALUES ('服务器A', '机房', '正常', '是', '服务器', '2024-01-01', '2025-03-01', '可用');

-- 建表语句
CREATE TABLE  IF NOT EXISTS xitongshezhi_kongjianshujuguanli (
    id INT PRIMARY KEY AUTO_INCREMENT,
    didian VARCHAR(100) NOT NULL,
    leixing VARCHAR(100),
    shuoming VARCHAR(100)
);
-- 测试数据插入
INSERT INTO xitongshezhi_kongjianshujuguanli (didian, leixing, shuoming)
VALUES ('校园地图', '位置数据', '教学楼、宿舍区位置信息');

-- 建表语句
CREATE TABLE  IF NOT EXISTS guizepeizhi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    guizemingchen VARCHAR(100) NOT NULL,
    guizeleixing VARCHAR(100),
    guizemiaoshu VARCHAR(100)
);
-- 测试数据插入
INSERT INTO guizepeizhi (guizemingchen, guizeleixing, guizemiaoshu)
VALUES ('考勤规则', '人员管理', '每日9点前打卡');

-- 建表语句
CREATE TABLE  IF NOT EXISTS xitongshezhi_kyonghuguanli (
    id INT PRIMARY KEY AUTO_INCREMENT,
    xingming VARCHAR(100) NOT NULL,
    xingbie VARCHAR(100),
    dengluzhanghao VARCHAR(100),
    shouji VARCHAR(50),
    xingzhengquyu VARCHAR(100),
    bumen VARCHAR(100),
    juese VARCHAR(50)
);
-- 测试数据插入
INSERT INTO xitongshezhi_kyonghuguanli (xingming, xingbie, dengluzhanghao, shouji, xingzhengquyu, bumen, juese)
VALUES ('系统管理员', '男', 'admin', '13011112222', '北京市', 'IT部', '超级管理员');

-- 建表语句
CREATE TABLE  IF NOT EXISTS chufaguize (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cfgz VARCHAR(100) NOT NULL,
    neirong VARCHAR(100)
);
-- 测试数据插入
INSERT INTO chufaguize (cfgz, neirong)
VALUES ('迟到处罚', '迟到30分钟以内扣50元');

-- 建表语句
CREATE TABLE  IF NOT EXISTS weixianshijianchufaguize (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cfgz VARCHAR(100) NOT NULL,
    neirong VARCHAR(100)
);
-- 测试数据插入
INSERT INTO weixianshijianchufaguize (cfgz, neirong)
VALUES ('火灾处理', '立即启动消防预案');

-- 建表语句
CREATE TABLE  IF NOT EXISTS excelchangshi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    diyilie VARCHAR(100),
    dierlie VARCHAR(100),
    disanlie VARCHAR(100),
    disilie VARCHAR(100),
    diwulie VARCHAR(100)
);
-- 测试数据插入
INSERT INTO excelchangshi (diyilie, dierlie, disanlie, disilie, diwulie)
VALUES ('姓名', '年龄', '性别', '部门', '职位');