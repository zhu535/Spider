# -*- coding: utf-8 -*-
# @Time : 2020/2/18 17:47
# @Author : zhu
# @FileName: 1.3_requests的post请求.py
# @Software: PyCharm

import requests

url = 'https://fanyi.baidu.com/sug'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

data = {'kw':'哈哈哈'}

res = requests.post(url=url, headers=headers, data=data)

code = res.status_code
print(code)

if code == 200:
    print(res.json())