from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH =r"C:\Users\Admin\OneDrive\Desktop\webdriver\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.aeb.am/")
driver.maximize_window()

aeb_online = driver.find_element (By.LINK_TEXT, "AEB Online")
aeb_online.click()
sleep(1)

user_input = driver.find_element (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[1]/label/div/input')
user_input.send_keys('lil2022111@gmail.com')

password_input = driver.find_element (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[2]/label/div/input')
password_input.send_keys('Abc123.')

sign_in_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[4]/button')
sign_in_button.click()
sleep(10)

driver.quit()