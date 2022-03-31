from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()

service_1 = driver.find_element(By.CSS_SELECTOR, "#top_menu > div:nth-child(3) > a > span")
service_1.click()

sleep(2)
payment = driver.find_element(By.LINK_TEXT, "AEB payments")
payment.click()

sleep(2)

payment_loan= driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/div[1]/div')
sleep(2)

payment_loan.click()

