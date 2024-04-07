from time import sleep

from config.driver_config import DriverConfig
from page.loginPage import LoginPage


class TestLogin:
    def test_login(self,driver):

        LoginPage().login(driver=driver,user="william")
        sleep(3)

