from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 1700)")
rate = driver.find_element(By.XPATH, '//*[@id="homepage"]/div[5]/div/div[3]/div/div[2]/div/div[1]')
rate.click()

sleep(2)

driver.quit