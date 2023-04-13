#-*- coding:utf8 -*-
import os
import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# sign in
def sign_in_club(driver):
    for retry in range(3):
        driver.get("https://bbs.elecfans.com/plugin.php?id=dsu_paulsign:sign")
        time.sleep(5)

        try:
            element = driver.find_element(By.XPATH, '//*[@id="wp"]/div[2]/div[2]/p[2]/a')
        except Exception as e:
            logging.error("Error message : {0}".format(e))
            return
        else:
            title = element.get_attribute("title")
            if title == u"我要签到":
                element.click()
            else:
                return

        time.sleep(10)

        try:
            element = driver.find_element(By.XPATH, '//*[@id="kx"]')
        except Exception as e:
            logging.error("Error message : {0}".format(e))
            continue
        else:
            element.click()

        element = driver.find_element(By.XPATH, '//*[@id="qiandao"]/div/table[2]/tbody/tr[1]/td/label[3]')
        element.click()

        element = driver.find_element(By.XPATH, '//*[@id="qiandao"]/p/button')
        print(element.text)
        element.click()
        break

# login in
def login_in_club(user_name, pass_word):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(options=option)
    driver.set_window_size(1024, 768)
    driver.maximize_window()

    for retry in range(3):
        driver.get("https://passport.elecfans.com/login?referer=https://bbs.elecfans.com/./&siteid=4&scene=bbspage&account=&fromtype=undefined#https%3A%2F%2Fbbs.elecfans.com%2Fmember.php%3Fmod%3Dlogging%26action%3Dlogin")
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/p[2]/span[2]').click()
        time.sleep(3)
        element = driver.find_element(By.NAME, "account")
        element.send_keys(user_name)
        element = driver.find_element(By.NAME, "password")
        element.send_keys(pass_word)
        driver.find_element(By.XPATH, '/html/body/div[1]/form[1]/div[5]/button').click()
        time.sleep(8)

        current_url = driver.current_url
        if current_url != "https://bbs.elecfans.com/":
            logging.error("account or password error, please check it, login in failed!");
            continue
        else:
            break

    if current_url != "https://bbs.elecfans.com/":
        logging.error("login in failed!");
        return None

    try:
        element = driver.find_element(By.ID, "useritem")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
        return None

    try:
        element.click()
    except Exception as e:
        logging.error("Error message : {0}".format(e))
        return None
    else:
        logging.info("sign in success!")

    time.sleep(2)

    score_num = None
    # check score
    try:
        element = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[1]/div[2]/div[2]/span[2]")
    except Exception as e:
        logging.error("Error message : {0}".format(e))
    else:
        score_num = element.text[3:]
        logging.info("signed in scores : {0}".format(score_num))

    sign_in_club(driver)

    driver.quit()

    return score_num
