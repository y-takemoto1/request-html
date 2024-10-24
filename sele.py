from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import streamlit as st

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

target_url = 'https://jp.indeed.com/jobs?q=%E6%AD%A3%E7%A4%BE%E5%93%A1&l=%E7%A6%8F%E5%B2%A1%E7%9C%8C&from=searchOnDesktopSerp&vjk=d4bb56841be7498e'
driver.get(target_url)

wait = WebDriverWait(driver, 10)
risult = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job_seen_beacon')))

elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

for element in elements:
    print(element.find_element(By.CSS_SELECTOR, 'jobTitle jobTitle-newJob css-1psdjh5 eu4oa1w0').text)

time.sleep(15)
driver.quit()