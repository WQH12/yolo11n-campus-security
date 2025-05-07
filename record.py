import time as t


class ETimer:
    """创建一个计时器的类"""

    # 初始化一些可能会用到的变量
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = 0

    # 开始计时
    def start(self):
        self.begin = t.time()
        print("计时开始...")

    # 停止计时,并显示持续时间
    def stop(self):
        self.end = t.time()
        print("计时结束...")
        self.lasted = self.end - self.begin
        # 报出持续时间
        print(f'持续了{self.lasted}秒')