from selenium import webdriver
from time import sleep

from common.tools import get_project_path, sep
from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()

driver.get("https://www.baidu.com")
sleep(3)

driver.quit()
