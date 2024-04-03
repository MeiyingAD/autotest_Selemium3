from time import sleep

from config.driver_config import DriverConfig
from page.loginPage import LoginPage

class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        driver.get("http://www.tcpjwtester.top")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "1234abcd!")
        sleep(1)
        LoginPage().click_login(driver, "登录")
        sleep(3)
        driver.quit()
