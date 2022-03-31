from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()

deposit = driver.find_element(By.XPATH, '//*[@id="avand_type"]/option[1]')
deposit.click()

amount = driver.find_element(By.ID, "avand_amount1")
amount.send_keys("1000000")

term = driver.find_element(By.ID, "avand_days1")
term.send_keys("500")

sleep(5)

calculate = driver.find_element(By.XPATH, '//*[@id="avand_form"]/div[3]/div')
calculate.click()

sleep(5)

driver.quit()