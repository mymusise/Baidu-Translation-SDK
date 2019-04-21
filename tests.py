from baidu_translate import TranslateClient


client = TranslateClient()
print(client.auto2auto('你好, 这是个测试').text)
print(client.zh2en('你好, 这是个测试').text)
print(client.en2zh('Hello').text)