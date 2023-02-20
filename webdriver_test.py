#-*- coding:utf8 -*-
import os
import sys
import time
import logging
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "zh-CN,zh;q=0.9", 
    "Host": "httpbin.org", 
    "Referer": "https://blog.csdn.net/XnCSD/article/details/88615791", 
    "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-63f33582-5b8745f923bca1bf6ab14c5d"
"""

url = 'https://httpbin.org/headers'

user_agent = "Mozilla/5.1 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.1.1.1 Safari/537.36"

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('no-sandbox')
option.add_argument('disable-dev-shm-usage')
# option.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(options=option)
driver.set_window_size(1024, 768)
driver.maximize_window()

driver.get(url)

print(driver.page_source)
with open("headers.txt", "w") as f:
    f.write(driver.page_source)

driver.close()

