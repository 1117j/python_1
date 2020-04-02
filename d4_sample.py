import time
from selenium.webdriver import Chrome

chromeDriver = 'C:\\temp\\chromeDriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://login.11st.co.kr/auth/front/login.tmall')

time.sleep(2)  #()초동안 멈추게하는거

input_login = driver.find_element_by_id("loginName")
input_login.send_keys("luvhj6411")

input_pw = driver.find_element_by_id("passWord")
input_pw.send_keys("hj")

btn = driver.find_element_by_class_name("btn_Atype")

time.sleep(2)

btn.click()

time.sleep(55)

driver.get()
# driver.quit()


