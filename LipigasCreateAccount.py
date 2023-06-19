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



def Create(correo,nombre,apellido,password,telefono,rut):

        driver=webdriver.Chrome(driver_path,chrome_options=options)
        driver.get('https://sucursal.lipigas.cl/app_sucursal/frontend/usuarios/registro')

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.NAME,'cliente')))\
                        .click()
        '''
        selectdia = Select(driver.find_element_by_id('days'))
        selectdia.select_by_value(str(dia))
        '''    
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div/div/form/button')))\
                        .click()

        time.sleep(1)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'rut')))\
                        .send_keys(rut)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'nombre')))\
                        .send_keys(nombre)
        

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'apellidos')))\
                        .send_keys(apellido)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'clave')))\
                        .send_keys(password)
        
        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'clave2')))\
                        .send_keys(password)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'telefono')))\
                        .send_keys(telefono)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'email')))\
                        .send_keys(correo)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID,'r-email')))\
                        .send_keys(correo)

        element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div/div/form/div[4]/ul/li[2]/button')))\
                        .click()
        time.sleep(10)
        driver.close()
