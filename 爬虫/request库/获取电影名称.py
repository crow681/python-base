#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 23:07
# @Author  : wangjun
# @File    : 获取电影名称.py
# @explain : 爬取豆瓣top250电影名

import requests
from bs4 import BeautifulSoup

def get_douban_movie_250():
    """

    :return: 电影名称列表
    """
    url = 'https://movie.douban.com/top250?' # 第一页
    headers = {
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1 Edg/104.0.5112.81'
    }
    list_name = []
    for i in range(0, 10):
        link = f'{url}start={i}'
        r = requests.post(link, headers=headers, timeout=5)
        data = r.text

        soup = BeautifulSoup(data, 'lxml')
        title = soup.find_all('span', 'title')

        for index in title:
            name = index.text   # 获取电影名称
            if '/' not in name:  # 去掉英文名
                list_name.append(name)
    return list_name


if __name__ == '__main__':
    movie_name = get_douban_movie_250()
    # print(movie_name)
    with open('../电影名.txt', 'w', encoding='utf-8') as file:
        for name in movie_name:
            file.write(name+'\n')