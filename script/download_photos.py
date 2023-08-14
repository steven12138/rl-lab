# -*- coding: UTF-8 -*-
"""
@Project ：rl-lab 
@File    ：download_photos.py
@Author  ：Yifu Yuan
@Date    ：2023/8/14
"""
import openpyxl
import requests
import os

workbook = openpyxl.load_workbook('team_info.xlsx')
worksheet = workbook.active
photo = worksheet['H'][1:]
name = worksheet['B'][1:]

for i in range(len(name)):
    url = photo[i].value
    response = requests.get(url)
    photo_path = f'../assets/image/team/{name[i].value}.jpg'
    if not os.path.exists(photo_path):
        with open(photo_path, 'wb') as f:
            f.write(response.content)

print("End")