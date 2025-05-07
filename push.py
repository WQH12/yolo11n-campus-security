

from send_message import SendMessage


class PUSH(object):
    def __init__(self,event1,location1,name1,time1,ps1) -> None:
        self.event=event1;
        self.location = location1;
        self.name = name1;
        self.time = time1;
        self.ps = ps1;


    def push(self) -> None:
        # 实例SendMessage
        sm = SendMessage()
        # 获取接口返回数据
        json_data = {"event": self.event, "location":self.location , "name": self.name, "time": self.time, "ps": self.ps}
        # 发送消息
        sm.send_message(json_data=json_data)


