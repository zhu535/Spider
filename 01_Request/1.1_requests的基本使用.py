# -*- coding: utf-8 -*-
# @Time : 2020/2/18 10:48
# @Author : zhu
# @FileName: 1.1_requests的基本使用.py
# @Software: PyCharm

import requests

# 发起请求
url = 'https://www.baidu.com/'

res = requests.get(url)

print(res)              # <Response [200]> 状态码
print(res.content)      # b'...'二进制的文本流
print(res.content.decode('utf-8'))  # 解码
print(res.text)         # 和上面是一样的
print(res.headers)      # {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 18 Feb 2020 03:34:33 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
print(res.status_code)  # 200
print(res.request.headers)    # {'User-Agent': 'python-requests/2.19.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
