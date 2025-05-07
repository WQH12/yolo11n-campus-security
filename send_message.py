import json
import requests
from access_token import AccessToken


class SendMessage(object):
    # 消息接收者
    TOUSER = 'og3Rz6on84WE_WEpJ9osAn41aQ4s'
    # 消息模板id
    TEMPLATE_ID = 'vihTefhzqP9rwj-0h7st966QSPlXEMB2E5xmJ0YPahI'
    # 点击跳转链接（可无）
    CLICK_URL = 'https://api.weixin.qq.com/cgi-bin/media/get?access_token=67_gV0_VahIzBE9G_60hjOOR4iPQ_c9hzL11r3mb6x59rxSqOLSwDDoJG_srTxRJJlnJQ_PHZ9VFhNZZR81HLd79T9SLkf4SWYv5tNHvj51CRDFHyV5RfFqrdvBkRERWDaABAKPW&media_id=MmU0RoFsyutjL-MweRM_q6axbzMZgg3Aa1hKuXYs4QOn1Z7AdlzwGA41GJSIRdGa'  #这块以后还是很有用的

    def __init__(self, touser=TOUSER, template_id=TEMPLATE_ID, click_url=CLICK_URL) -> None:
        """
        构造函数
        :param touser: 消息接收者
        :param template_id: 消息模板id
        :param click_url: 点击跳转链接（可无）
        """
        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id
        self.click_url = click_url

    def get_send_data(self, json_data) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": self.click_url,
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "event": {
                    "value": json_data["event"],
                    # 字体颜色
                    "color": "#173177"
                },
                "location": {
                    "value": json_data["location"],
                    "color": "#173177"
                },
                "name": {
                    "value": json_data["name"],
                    "color": "#173177"
                },
                "time": {
                    "value": json_data["time"],
                    "color": "#173177"
                },
                "ps": {
                    "value": json_data["ps"],
                    "color": "#173177"
                },

            }
        }

    def send_message(self, json_data) -> None:
        """
        发送消息
        :param json_data: json数据
        :return:
        """
        # 模板消息请求地址
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()
        # 有关响应结果，我有整理成xml文档（官方全1833条），免费下载：https://download.csdn.net/download/sxdgy_/86263090
        if result["errcode"] == 0:
            print("消息发送成功")
        else:
            print(result)
