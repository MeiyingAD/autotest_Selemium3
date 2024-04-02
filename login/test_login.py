from william_chromedriver_manager.core import get_local_webdriver_path
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path=get_local_webdriver_path())

driver.get("http://192.168.31.156")

sleep(2)
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("1234abcd!")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)

driver.quit()
