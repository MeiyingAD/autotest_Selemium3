from william_chromedriver_manager.core import get_local_webdriver_path
from selenium import webdriver

driver = webdriver.Chrome(executable_path=get_local_webdriver_path())

driver.get("https://www.baidu.com")
