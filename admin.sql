-- 使用该数据库
USE flaskdata;

-- 创建 admin 表
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    adminname VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
-- 插入第一条测试数据
INSERT INTO admin (adminname, password)
VALUES ('admin1', '123');

-- 插入第二条测试数据
INSERT INTO admin (adminname, password)
VALUES ('admin2', '456');
--     -- 删除 admin 表
-- DROP TABLE IF EXISTS admin;  