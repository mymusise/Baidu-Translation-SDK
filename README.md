# Baidu Translation SDK

A unofficial SDK for Baidu Translation. 一个非官方的百度翻译SDK.


## Quick start

### 1.Installation

```
pip install baidu-translate-sdk
```


### 2. Add a environment variable

```
export BAIDU_TRANSLATE_API_AUTH="$auth-file"
```

The auth-file contains your service account key.

Example:
```json
{
    "APPID": "20129XXXXXX",
    "SECRETKEY": "NpAf7XXXXXXXX",
    "SERVER": "api.fanyi.baidu.com"
}
```


### 3. Example

```python
from baidu_translate import TranslateClient


client = TranslateClient()
print(client.auto2auto('你好, 这是个测试').text)
print(client.zh2en('你好, 这是个测试').text)
print(client.en2zh('Hello').text)
```

```
>>> Hello, this is a test.
>>> Hello, this is a test.
>>> 你好
```

### 4. Other language

- Use a quick method: `client.{from_lang}2{to_lang}(text)`
- Use translate function: `client.translate(text, from_lang='', to_lang='')`


### 5. Get the whole response
```
client._translate('Hello', 'en', 'jp')
```
```
>>> {'from': 'en', 'to': 'yue', 'trans_result': [{'dst': 'こんにちは', 'src': 'Hello'}]}
```


[More](https://api.fanyi.baidu.com/api/trans/product/apidoc)