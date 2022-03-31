from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()

sleep(1)
search_box = driver.find_element(By.XPATH, '//*[@id="header_search"]/div[1]')
sleep(2)
search_box.click()

search_box_1 = driver.find_element(By.NAME, 'q')
search_box_1.send_keys("loan"+Keys.ENTER)

searched_elements = driver.find_element(By.XPATH, '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]')
searched_data = searched_elements.find_elements(By.CSS_SELECTOR," div.gsc-thumbnail-inside > div > a")
for element in searched_data:
 
   if (element.text == "Online Loan"):
       element.click()
       break
sleep(2)

driver.quit()