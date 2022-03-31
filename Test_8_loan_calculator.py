from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()


amount = driver.find_element(By.ID, "loan_amount")
amount.send_keys("5000000")

currency = driver.find_element(By.XPATH, '//*[@id="loan_currency"]/option[3]')
currency.click()

term = driver.find_element(By.XPATH, '//*[@id="vark_form"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/label/span[1]')
term.click()

time = driver.find_element(By.ID, "loan_time")
time.send_keys("5")

rate = driver.find_element(By.ID, "loan_percent")
rate.send_keys("11")

sleep(2)

calculate = driver.find_element(By.XPATH, '//*[@id="vark_form"]/div[2]/div')
calculate.click()

sleep(10)

driver.quit()