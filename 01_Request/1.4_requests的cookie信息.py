# -*- coding: utf-8 -*-
# @Time : 2020/2/18 22:06
# @Author : zhu
# @FileName: 1.4_requests的cookie信息.py
# @Software: PyCharm

import requests

# 目标网址
# url = 'http://www.rrys2019.com/user/user'
url = 'https://account.geekbang.org/dashboard/info'
# 登陆请求网址
# login_url = 'http://www.rrys2019.com/User/Login/ajaxLogin'
login_url = 'https://account.geekbang.org/account/ticket/login'

# 请求头信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

# 使用session保存登陆的信息
# data = {'account': 'zhu170535',
#         'password': 'Zhu170535',
#         'remember': '0',
#         'url_back': 'http://www.rrys2019.com/user/user'
#         }

data = {'appid': '1',
        'captcha': "",
        'cellphone': "13126261405",
        'country': '86',
        'password': "zqz980629",
        'platform': '3',
        'remember': '1',
        'source': ""
        }

res = requests.session()

ret = res.post(url=login_url, headers=headers, data=data)

code = ret.status_code
print(code)

if code == 200:

    rett = res.get(url=url, headers=headers)
    print(rett.status_code)
    if rett.status_code == 200:

        with open('text.html', 'w', encoding='utf-8') as f:
            f.write(rett.text)

