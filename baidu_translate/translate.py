import hashlib
import urllib
from .client import Client


class TranslationRespon(object):

    def __init__(self, data):
        self.src = data['src']
        self.dst = data['dst']
    
    def __str__(self):
        return self.dst
    
    def __repr__(self):
        return self.__str__()
    
    @property
    def text(self):
        return self.dst


class TranslateClient(Client):
    _url = '/api/trans/vip/translate'
    LANG = ['zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra',
            'spa', 'th', 'ara', 'ru', 'pt', 'de', 'it',
            'el', 'nl', 'pl', 'bul', 'est', 'dan', 'fin',
            'cs', 'rom', 'slo', 'swe', 'hu', 'cht', 'vie',
            'auto']

    def __getattr__(self, name):
        if '2' in name:
            from_lang, to_lang = name.split('2')
            if from_lang in self.LANG and to_lang in self.LANG:
                return lambda q: self.translate(q, from_lang, to_lang)
        raise AttributeError(f"no attribute name: {name}")

    def set_sign(self, query):
        sign = self.appid + query + str(self.salt) + self.secret_key
        m = hashlib.md5(sign.encode())
        self.sign = m.hexdigest()

    def _translate(self, query, from_lang, to_lang):
        self.set_sign(query)
        params = {
            'q': urllib.parse.quote(query),
            'from': from_lang,
            'to': to_lang
        }
        return self.get(params).json()

    def translate(self, query, from_lang, to_lang):
        res = self._translate(query, from_lang, to_lang)
        result = [TranslationRespon(result) for result in res['trans_result']]
        if len(result) == 1:
            return result[0]
        return result

    def zh2en(self, query):
        return self.translate(query, 'zh', 'en')

    def en2zh(self, query):
        return self.translate(query, 'en', 'zh')

