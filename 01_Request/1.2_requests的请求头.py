# -*- coding: utf-8 -*-
# @Time : 2020/2/18 17:15
# @Author : zhu
# @FileName: 1.2_requests的请求头.py
# @Software: PyCharm

import requests

url = 'https://www.xicidaili.com/nn/'

# 伪造请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

}

res = requests.get(url= url, headers= headers)

# 获取状态码
print(res.status_code)

if res.status_code == 200:
    with open('baidu.html', 'w', encoding= 'utf-8') as f:
        f.write(res.text)