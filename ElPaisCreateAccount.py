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



def Create(correo,password,dia,mes,año):

        driver=webdriver.Chrome(driver_path,chrome_options=options)
        driver.get('https://elpais.com/subscriptions/#/register?prod=REG5D&o=CABEP&backURL=https%3A%2F%2Fcincodias.elpais.com%2F%3Fevent_log%3Doklogin')

        time.sleep(3)
        try:
            element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/button[2]')))\
                            .click()
        except:
            None
        time.sleep(3)
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.NAME,'subsEmail')))\
                        .send_keys(correo)
        '''
        selectdia = Select(driver.find_element_by_id('days'))
        selectdia.select_by_value(str(dia))
        '''    
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.NAME,'subsPassword')))\
                        .send_keys(password)
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.NAME,'subsConfirmPassword')))\
                        .send_keys(password)

        selectdia = Select(driver.find_element_by_xpath('/html/body/div[3]/article/div/div/div/div[2]/div[9]/div[1]/div[1]/select'))
        selectdia.select_by_value(str(dia))
        selectmes = Select(driver.find_element_by_xpath('/html/body/div[3]/article/div/div/div/div[2]/div[9]/div[1]/div[2]/select'))
        selectmes.select_by_value(str(mes))
        selectaño = Select(driver.find_element_by_xpath('/html/body/div[3]/article/div/div/div/div[2]/div[9]/div[1]/div[3]/select'))
        selectaño.select_by_value(str(año))

        
        
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/article/div/div/div/div[2]/div[10]/div[1]/label')))\
                        .click()
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'subsSignUp')))\
                        .click()

        time.sleep(10)
        driver.close()
Create('brian.castro@mail.udp.cl','Briancastro1',9,3,2000)
