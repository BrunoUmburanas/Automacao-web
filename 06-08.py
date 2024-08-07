from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



drive=webdriver.Chrome()
drive.get('https://www.saucedemo.com/')
sleep(1)

user_name=drive.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input' )

user_name.send_keys('standard_user')
sleep(0.3)

user_password=drive.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input' )
user_password.send_keys('secret_sauce')
sleep(0.3)
botao_login= drive.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/input')
botao_login.click()
sleep(0.3)
add_camisetaPret=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
add_camisetaPret.click()
sleep(0.3)
car_bot=drive.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
car_bot.click()
sleep(0.3)
check_bot=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/button[2]')
check_bot.click()
sleep(0.3)
fir_name=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input')
fir_name.send_keys('Bruno')
sleep(0.3)
last_name=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input')
last_name.send_keys('Umburanas')
sleep(0.5)
post_code=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input')
post_code.send_keys('123456')
sleep(0.5)
botao_continue = drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[2]/input')
botao_continue.click()
sleep(0.5)
finish_botao=drive.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')
finish_botao.click()


sleep(5)