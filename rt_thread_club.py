#-*- coding:utf8 -*-
import os
import sys
import time
import logging
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_in_club(user_name, pass_word):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(options=option)
    driver.set_window_size(1024, 768)
    driver.maximize_window()
    # login in
    for i in range(3):
        driver.get("https://www.rt-thread.org/account/user/index.html?response_type=code&authorized=yes&scope=basic&state=1588816557615&client_id=30792375&redirect_uri=https://club.rt-thread.org/index/user/login.html")
        element = driver.find_element(By.ID, "username")
        element.send_keys(user_name)
        element = driver.find_element(By.ID, 'password')
        element.send_keys(pass_word)
        driver.find_element(By.ID, 'login').click()
        time.sleep(8)

        current_url = driver.current_url
        if current_url != "https://club.rt-thread.org/":
            logging.error("username or password error, please check it, login in failed!");
            time.sleep(60)
            continue
        else:
            break

    if current_url != "https://club.rt-thread.org/":
        logging.error("login in failed!");
        return None

    try:
        element = driver.find_element(By.LINK_TEXT, u"立即签到")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
    else:
        try:
            element.click()
        except Exception as e:
            logging.error("Error message : {0}".format(e))
            return None
        else:
            logging.info("sign in success!")

    time.sleep(2)

    day_num = None
    # check sign in days
    try:
        element = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/a")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
    else:
        day_num = element.text
        logging.info("signed in today : {0}".format(day_num))
        # driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/h3/div/a').click()
        # time.sleep(3)
        # driver.get_screenshot_as_file("./paihang.png")
        # driver.find_element(By.XPATH, '/html/body/div[9]/span[1]/a').click()

    driver.refresh()
    time.sleep(2)

    weekday = time.localtime().tm_wday
    if weekday == 6:
        elements = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div/div/div')
        li = random.randint(0, 5)
        element = elements[li].find_element(By.XPATH, 'a')
        driver.get(element.get_attribute("href"))
        time.sleep(5)
        element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/a[1]')
        element.click()

    driver.quit()

    return day_num
