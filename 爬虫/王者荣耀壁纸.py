#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 23:25
# @Author  : wangjun
# @File    : 王者荣耀壁纸.py

import requests

url = "https://shp.qpic.cn/ishow/2735061016/1654848352_1265602313_31815_sProdImgNo_2.jpg/0"
heard = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Host': 'shp.qpic.cn',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
img = requests.get(url=url, headers=heard)
response = img.text.encode('utf-8')
print(response)