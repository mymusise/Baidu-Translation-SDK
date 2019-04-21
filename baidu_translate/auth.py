import os
import json
import random


class BaiduAuth(object):

    def __init_auth_file(self, auth_file):
        auth_data = json.load(open(auth_file))
        self.appid = auth_data.get('APPID')
        self.secret_key = auth_data.get('SECRETKEY')
        self.server = auth_data.get('SERVER', 'api.fanyi.baidu.com')

    def __init_salt(self):
        return random.randint(32768, 65536)

    def __init__(self):
        self.__init_auth_file(os.environ['BAIDU_TRANSLATE_API_AUTH'])
        self.salt = self.__init_salt()
        self.sign = ''
