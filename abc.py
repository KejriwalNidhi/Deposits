from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver import ActionChains
import csv

ques_url= str(input("enter question:\n"))

driver = webdriver.chrome('')
driver.get(ques_url)
bottom_of_the_page_xpath = '//div[@class="spinner_display_area_hidden"]'
print("\n")
    
