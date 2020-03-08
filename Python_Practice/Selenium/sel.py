from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path=r"C:\Users\HD PC\Desktop\Danish\Udemy\Django_and_Python_Tutorials\Python_Practice\Selenium\chromedriver.exe")
browser.maximize_window()
# assert 'Youtube' in browser.title
#Create a new Google chrome session
#Navigate to the application home page
browser.get('http://www.youtube.com/')

# get the search textbox

search_field = browser.find_element_by_xpath("//input[@id='search']")

search_field.send_keys("Selenium WebDriver Interview questions")
search_field.send_keys(Keys.RETURN)

#browser.quit()
