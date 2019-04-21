import requests
from .auth import BaiduAuth
import logging


logger = logging.getLogger('baidu-translation')


class Client(BaiduAuth):
    _url = ''

    @property
    def url(self):
        return f"https://{self.server}{self._url}"

    def check_params(self, params):
        if 'appid' not in params:
            params['appid'] = self.appid
        if 'salt' not in params:
            params['salt'] = self.salt
        if 'sign' not in params:
            params['sign'] = self.sign

    def get(self, params):
        self.check_params(params)
        param_str = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{self.url}?{param_str}"
        logger.info(f"getting url: {url}")
        return requests.get(url, timeout=2)

