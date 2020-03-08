from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(executable_path=r"C:\Users\HD PC\Desktop\Danish\Udemy\Django_and_Python_Tutorials\Python_Practice\Selenium\chromedriver.exe")

browser.get('http://www.youtube.com/')
