

import requests


class AccessToken(object):
    # 微信公众测试号账号（填写自己的）
    APPID = "wxec81c23accb8e9f3"
    # 微信公众测试号密钥（填写自己的）
    APPSECRET = "7b23b92b2fe51c6cd805e71c8c068949"

    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:
        """
        获取access_token凭证
        :return: access_token
        """
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)
